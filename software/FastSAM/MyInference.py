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




import cv2
import zmq
import base64
import numpy as np

image_buffer = []

class VideoClient:
    def __init__(self):
        # Initialize ZMQ socket and other necessary variables
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.PAIR)
        self.footage_socket.bind('tcp://*:5555')  # Update the address as needed
        print("Client Initialized")

    def receive_video(self):
        global image_buffer
        print("Client Start Receive Video")
        while True:
            frame = self.footage_socket.recv_string()
            img = base64.b64decode(frame)
            npimg = np.frombuffer(img, dtype=np.uint8)
            source = cv2.imdecode(npimg, 1)

            cv2.imwrite('image.png', source)
            
            print("write to file")
            # cv2.imshow("Stream", source)
            # Process the frame (e.g., display, or pass to another function)
            cv2.waitKey(1)


def Detect():

    print("Start Detect")

    while True:
        model_path = "./weights/FastSAM-s.pt"
        img_path = "image.png"
        model = FastSAM(model_path)
        point_prompt = ast.literal_eval("[[480, 320]]")

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

        print(".")
        sys.exit()

        prompt_process = FastSAMPrompt(input, everything_results, device=device)

        # process point promt
        ann = prompt_process.point_prompt(
            points = point_prompt, pointlabel = point_label
        )
        points = point_prompt
        point_label = point_label

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
    # Create the client instance
    client = VideoClient()

    # Create a thread for receiving video
    video_thread = threading.Thread(target=lambda: client.receive_video())
    video_thread.start()

    # Create a thread for detection
    detect_thread = threading.Thread(target=Detect)
    detect_thread.start()

    # Optionally, wait for the detect thread to finish
    # detect_thread.join()

    # Note: We're not joining the video_thread as it's an infinite loop
    


if __name__ == "__main__":
    main()
