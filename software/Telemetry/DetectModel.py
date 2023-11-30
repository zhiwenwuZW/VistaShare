from ultralytics import RTDETR
import cv2
import numpy as np
from PIL import Image
import zmq
import base64


class Detector:
    def __init__(self):
        # Initialize ZMQ context and socket
        self.context = zmq.Context()
        self.footage_socket = self.context.socket(zmq.PAIR)
        self.footage_socket.bind('tcp://*:5556')
        print("Client Init")
        self.frame_cnt = 0

    def receive(self):
        frame = self.footage_socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.frombuffer(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        # print("Received")
        cv2.imshow("Stream", source)
        cv2.waitKey(1)
        source_rgb = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
        self.input = Image.fromarray(source_rgb)
        self.frame_cnt = self.frame_cnt + 1

    def detect(self):
        # Load the model
        model = RTDETR('rtdetr-l.pt')

        # Run inference
        # only keep 4 objects: 2: cars  5: bus 7: truck 9: traffic light 10:fire hydrant 11: stop sign 
        results = model(self.input, stream=True, classes = [0, 2, 5, 7, 9, 10, 11])

        for result in results:
            # Calculate the center of the image
            img_center_x = result.orig_shape[1] / 2
            img_center_y = result.orig_shape[0] *2 / 3

            print("pic center is:" + str(img_center_x) + " " + str(img_center_y))

            # for box in result.boxes.xyxy:
            #     x1, y1, x2, y2 = box
            #     if x1 <= img_center_x <= x2 and y1 <= img_center_y <= y2:
            #         # print("Box containing the center:", box)


            # print("### Visualize")
            # Visualize the detections
            annotated_image = result.plot(masks=False, prob=False, conf=False, labels=True)
            cv2.imshow('Detected Objects', annotated_image)

if __name__ == "__main__":
    detector = Detector()
    print("Start Detect")
    while True:
        detector.receive()
        if detector.frame_cnt > 3: 
            detector.detect()
            detector.frame_cnt = 0