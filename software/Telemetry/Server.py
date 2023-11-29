import cv2
import zmq
import base64
import picamera
from picamera.array import PiRGBArray

print("Server Starting")
IP = '192.168.105.228'

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(640, 480))

context = zmq.Context()
footage_socket = context.socket(zmq.PAIR)
footage_socket.connect(f'tcp://{IP}:5556')
print(f"Target IP: {IP}")

try:
    cnt = 0
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        if cnt > 10:
            frame_image = frame.array
            encoded, buffer = cv2.imencode('.jpg', frame_image)
            jpg_as_text = base64.b64encode(buffer)
            footage_socket.send(jpg_as_text)
            cnt = 0
        else: 
            cnt = cnt + 1
        rawCapture.truncate(0)
except KeyboardInterrupt:
    print("Interrupted by user")
    footage_socket.close()
    context.term()
    camera.close()
    print("Resource Freed")
