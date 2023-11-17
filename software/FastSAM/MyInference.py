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
import zmq
import base64

class FastSAMDetector:
    def __init__(self):
        # Initialize ZMQ context and socket
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.PAIR)
        self.footage_socket.bind('tcp://*:5556')
        print("Client Init")

        # Set up configurations
        self.model_path = "./weights/FastSAM-x.pt"
        self.model = FastSAM(self.model_path)
        self.img_path = "image.jpg"
        self.point_prompt = ast.literal_eval("[[320, 240]]")
        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else
            "mps" if torch.backends.mps.is_available() else
            "cpu"
        )
        self.retina = True
        self.imgsz = 640
        self.conf = 0.4
        self.iou = 0.9
        self.output = "./output/"
        self.withContours = True
        self.better_quality = False
        self.randomcolor = True
        self.bboxes = None
        self.points = None
        self.point_label = [1]
        self.box_prompt = convert_box_xywh_to_xyxy(ast.literal_eval("[[0,0,0,0]]"))
        self.is_point_prompt = True

        print("Prompt Init")

    def receive(self):
        frame = self.footage_socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.frombuffer(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        print("Received")
        cv2.imshow("Stream", source)

        source_rgb = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
        self.input = Image.fromarray(source_rgb)

    def detect(self):
        everything_results = self.model(
            self.input,
            device=self.device,
            retina_masks=self.retina,
            imgsz=self.imgsz,
            conf=self.conf,
            iou=self.iou    
        )

        prompt_process = FastSAMPrompt(self.input, everything_results, device=self.device)
        
        if self.is_point_prompt:
            ann = prompt_process.point_prompt(
                points=self.point_prompt, pointlabel=self.point_label
            )
            self.points = self.point_prompt
        else:
            ann = prompt_process.box_prompt(bboxes=self.box_prompt)
            self.bboxes = self.box_prompt

        prompt_process.plot(
            annotations=ann,
            output_path=self.output+self.img_path.split("/")[-1],
            bboxes=self.bboxes,
            points=self.points,
            point_label=self.point_label,
            withContours=self.withContours,
            better_quality=self.better_quality,
        )


if __name__ == "__main__":
    detector = FastSAMDetector()
    print("Start Detect")
    while True:
        detector.receive()
        detector.detect()
