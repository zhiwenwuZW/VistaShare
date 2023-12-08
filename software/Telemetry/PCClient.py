import socket
import pickle
import struct
import cv2

# Set up UDP socket
udp_ip = "0.0.0.0"
udp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

while True:
    # Receive size of data
    size, _ = sock.recvfrom(4)
    size = struct.unpack(">L", size)[0]

    # Receive data
    data, _ = sock.recvfrom(size)
    im_array, boxes = pickle.loads(data)