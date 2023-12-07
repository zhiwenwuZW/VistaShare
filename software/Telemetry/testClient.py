import cv2
import socket
import numpy as np

# Create a socket for receiving the video
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 10001))

print("Client up")

# Stream reception loop
while True:
    packet, _ = sock.recvfrom(65536)
    nparr = np.frombuffer(packet, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if frame is not None:
        cv2.imshow('Video Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()
sock.close()
