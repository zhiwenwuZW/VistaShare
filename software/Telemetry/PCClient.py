import socket
import pickle
import struct
import cv2

# Set up UDP socket
udp_ip = "0.0.0.0"
udp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((udp_ip, udp_port))

print("Client up")

def receive_chunks(sock, expected_size):
    received_data = b''
    while len(received_data) < expected_size:
        chunk, _ = sock.recvfrom(65507)
        received_data += chunk
    return received_data

while True:
    # Receive size of data
    size, _ = sock.recvfrom(4)
    size = struct.unpack(">L", size)[0]

    # Receive data
    data = receive_chunks(sock, size)
    im_array, boxes = pickle.loads(data)

    print(im_array)