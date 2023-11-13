import argparse
from fastsam import FastSAM, FastSAMPrompt 
import ast
import torch
from PIL import Image
from utils.tools import convert_box_xywh_to_xyxy


def main():
    # load model
    model_path = "./weights/FastSAM-s.pt"
    img_path = "./images/car.png"
    model = FastSAM(model_path)
    point_prompt = ast.literal_eval("[[480, 320]]")
    # TODO
    input = Image.open(img_path)
    
    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "mps"
        if torch.backends.mps.is_available()
        else "cpu"
    )
    # draw high-resolution segmentation masks
    retina = True
    # image size
    imgsz = 640
    # object confidence threshold
    conf = 0.4
    # iou threshold for filtering the annotations
    iou = 0.9
    # image save path
    output = "./output/"
    # draw the edges of the masks
    withContours = True
    # better quality using morphologyEx
    better_quality = False
    # mask random color
    randomcolor = True

    input = input.convert("RGB")
    everything_results = model(
        input,
        device=device,
        retina_masks=retina,
        imgsz=imgsz,
        conf=conf,
        iou=iou    
        )
    bboxes = None
    points = None
    # [1,0] 0:background, 1:foreground
    point_label = [1]
    prompt_process = FastSAMPrompt(input, everything_results, device=device)
    if point_prompt[0] != [0, 0]:
        ann = prompt_process.point_prompt(
            points = point_prompt, pointlabel = point_label
        )
        points = point_prompt
        point_label = point_label
    else:
        ann = prompt_process.everything_prompt()
    prompt_process.plot(
        annotations=ann,
        # TODO
        output_path= output+img_path.split("/")[-1],
        bboxes = bboxes,
        points = points,
        point_label = point_label,
        withContours= withContours,
        better_quality=better_quality,
    )




if __name__ == "__main__":
    main()
