import cv2
import socket
from picamera import PiCamera
from picamera.array import PiRGBArray

print("Server Starting")
IP = '192.168.10.228'  # IP of the receiver
PORT = 5555  # Port of the receiver

camera = PiCamera()
camera.resolution = (480, 480)
camera.framerate = 1
rawCapture = PiRGBArray(camera, size=(480, 480))

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        print(".")
        frame_image = frame.array
        encoded, buffer = cv2.imencode('.jpg', frame_image)

        # Send the image over UDP
        udp_socket.sendto(buffer, (IP, PORT))

        rawCapture.truncate(0)

except KeyboardInterrupt:
    print("Interrupted by user")
    # Close the camera
    camera.close()
    # Close the UDP socket
    udp_socket.close()
    print("Camera and UDP socket resources have been freed.")
