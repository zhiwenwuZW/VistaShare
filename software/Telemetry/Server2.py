import cv2
import picamera
from picamera.array import PiRGBArray
import time
import datetime
import socket

print("Server Starting")
IP = '192.168.105.228'
PORT = 12346

# Initialize the camera and set up the stream
camera = picamera.PiCamera()
camera.resolution = (320, 240)
camera.framerate = 10
rawCapture = PiRGBArray(camera, size=(320, 240))

# Initialize UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# Function to wait until a specific target time
def wait_until(target_time):
    while datetime.datetime.now() < target_time:
        time.sleep(0.001)  # Sleep for 1 millisecond

# Set a future start time (e.g., 1 minute from now)
start_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
print(f"Start time set for {start_time}")

try:
    print("Waiting for synchronized start time...")
    wait_until(start_time)  # Wait until the start time

    print("Starting camera capture...")
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame_image = frame.array
        # Process the frame here (e.g., display, save, or send it)
        # Increase JPEG compression
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]  # Example: JPEG quality set to 70
        result, buffer = cv2.imencode('.jpg', frame_image, encode_param)

        # Encode the frame for transmission
        _, buffer = cv2.imencode('.jpg', frame_image)
        sock.sendto(buffer, (IP, PORT))
        # Clear the stream in preparation for the next frame
        rawCapture.truncate(0)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    camera.close()
    sock.close()
    print("Camera closed. Resource Freed")
