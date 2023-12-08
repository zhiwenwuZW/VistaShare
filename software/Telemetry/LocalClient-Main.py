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

# Set up TCP socket
tcp_ip = "192.168.52.228"
tcp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((tcp_ip, tcp_port))

for r in results:
    im_array = r.orig_img
    ids = r.boxes.id
    boxes = r.boxes.xywh

    data = pickle.dumps((im_array, ids, boxes))
    sock.sendall(struct.pack(">L", len(data)) + data)

sock.close()





