import socket
import pickle
import struct
from ultralytics import YOLO
import cv2

ip_addr = "127.0.0.1"
port = 8888

# Initialize YOLO model
model = YOLO('yolov8n.pt')
tcp_addr = f'tcp://{ip_addr}:{port}'
# using local ip_addr
# only keep objects: 2: cars  5: bus 7: truck 9: traffic light 10:fire hydrant 11: stop sign 
results = model(tcp_addr, stream=True, classes = [0, 2, 5, 7, 9, 10, 11])

# Set up UDP socket
udp_ip = "192.168.52.228"
udp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for r in results:
    im_array = r.orig_img
    
    boxes = r.boxes.xywh
    print(im_array)
    # # Serialize data
    # data = pickle.dumps((im_array, boxes))
    # size = len(data)

    # # Ensure data is sent in chunks that fit in UDP datagram
    # sock.sendto(struct.pack(">L", size), (udp_ip, udp_port))
    # sock.sendto(data, (udp_ip, udp_port))


