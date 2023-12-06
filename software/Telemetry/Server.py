import cv2
import time
import datetime
import socket

print("Server Starting")
IP = '192.168.105.228'
PORT = 12346

print("Init Camera")
# Initialize the camera
camera = cv2.VideoCapture(0, cv2.CAP_V4L2)  # 0 is the default camera
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
camera.set(cv2.CAP_PROP_FPS, 10)

print("Init sockect")
# Initialize UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Function to wait until a specific target time
def wait_until(target_time):
    while datetime.datetime.now() < target_time:
        time.sleep(0.001)  # Sleep for 1 millisecond

# Set a future start time (e.g., 5 seconds from now)
start_time = datetime.datetime.now() + datetime.timedelta(seconds=5)
print(f"Start time set for {start_time}")

try:
    print("Waiting for synchronized start time...")
    wait_until(start_time)  # Wait until the start time

    print("Starting camera capture...")
    while True:
        ret, frame = camera.read()
        if not ret:
            break  # Exit the loop if the frame is not captured successfully

        # Process the frame here (e.g., display, save, or send it)
        # Increase JPEG compression
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]  # Example: JPEG quality set to 70
        result, buffer = cv2.imencode('.jpg', frame, encode_param)

        # Encode the frame for transmission
        _, buffer = cv2.imencode('.jpg', frame)
        sock.sendto(buffer.tobytes(), (IP, PORT))

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    camera.release()
    sock.close()
    print("Camera closed. Resource Freed")
