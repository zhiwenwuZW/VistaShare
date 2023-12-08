import socket
import pickle
import struct
import cv2

# Set up TCP socket
tcp_ip = "0.0.0.0"
tcp_port = 12345
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((tcp_ip, tcp_port))
sock.listen(1)
conn, addr = sock.accept()

print("Connection established")

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

try:
    while True:
        lengthbuf = recvall(conn, 4)
        length, = struct.unpack(">L", lengthbuf)
        data = recvall(conn, length)
        im_array, ids, boxes = pickle.loads(data)

        # Process/display image and boxes here
        cv2.imshow('Received Image', im_array)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # print(boxes)

except KeyboardInterrupt:
    print("KeyboardInterrupt")

finally:
    conn.close()
    sock.close()