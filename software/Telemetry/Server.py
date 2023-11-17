import cv2
import zmq
import base64
import picamera
from picamera.array import PiRGBArray

print("Server Starting")
IP = '192.168.10.228'

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 20
rawCapture = PiRGBArray(camera, size=(640, 480))

context = zmq.Context()
footage_socket = context.socket(zmq.PAIR)
footage_socket.connect(f'tcp://{IP}:5556')
print(f"Target IP: {IP}")

try:
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame_image = frame.array
        encoded, buffer = cv2.imencode('.jpg', frame_image)
        jpg_as_text = base64.b64encode(buffer)
        footage_socket.send(jpg_as_text)
        rawCapture.truncate(0)
except KeyboardInterrupt:
    print("Interrupted by user")
    camera.close()
