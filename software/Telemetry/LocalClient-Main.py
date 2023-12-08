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


def send_chunks(data, sock, addr, chunk_size=65507):
    # Break data into chunks
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Send each chunk
    for chunk in chunks:
        sock.sendto(chunk, addr)

for r in results:
    im_array = r.orig_img
    
    boxes = r.boxes.xywh
    # print(im_array)

    data = pickle.dumps((im_array, boxes))
    send_chunks(data, sock, (udp_ip, udp_port))





