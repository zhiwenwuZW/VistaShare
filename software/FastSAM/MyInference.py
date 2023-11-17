import argparse
import time
from fastsam import FastSAM, FastSAMPrompt 
import ast
import torch
from PIL import Image
from utils.tools import convert_box_xywh_to_xyxy
import sys
import os
import cv2
import threading
import numpy as np

def Detect():

    print("Start Detect")

    # Set up Configures
    model_path = "./weights/FastSAM-s.pt"
    model = FastSAM(model_path)
    img_path = "../Telemetry/image.jpg"
    point_prompt = ast.literal_eval("[[240, 240]]")
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
    imgsz = 480
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
    bboxes = None
    points = None
    # [1,0] 0:background, 1:foreground
    point_label = [1]   
    # [[x,y,w,h],[x2,y2,w2,h2]] support multiple boxes
    box_prompt = "[[0,0,0,0]]"
    box_prompt = convert_box_xywh_to_xyxy(ast.literal_eval(box_prompt))

    is_point_prompt = True

    while True:

        print("load")

        input = Image.open(img_path)
        input = input.convert("RGB")
        everything_results = model(
            input,
            device=device,
            retina_masks=retina,
            imgsz=imgsz,
            conf=conf,
            iou=iou    
            )
        
        print("process")     

        prompt_process = FastSAMPrompt(input, everything_results, device=device)
        
        if is_point_prompt:
            print("point")
            # process point prompt
            ann = prompt_process.point_prompt(
                points = point_prompt, pointlabel = point_label
            )
            points = point_prompt
            point_label = point_label
        else:
            print("box")
            # Box point prompt        
            ann = prompt_process.box_prompt(bboxes=box_prompt)
            bboxes = box_prompt

        print("plot")
        prompt_process.plot(
            annotations=ann,
            output_path= output+img_path.split("/")[-1],
            bboxes = bboxes,
            points = points,
            point_label = point_label,
            withContours= withContours,
            better_quality=better_quality,
        )




def main():    
    Detect()
    
if __name__ == "__main__":
    main()
