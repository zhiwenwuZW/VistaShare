import cv2
import zmq
import base64
import numpy as np
import sys

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
            cv2.imshow("Stream", source)
            print(".")
            cv2.waitKey(1)


# # Example usage
if __name__ == "__main__":
    client = VideoClient()
    try:
        client.receive_video()
    except KeyboardInterrupt:
        print("Interrputed")
        sys.exit()