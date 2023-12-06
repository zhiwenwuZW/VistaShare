import cv2
import socket
import numpy as np

# Set the IP address and port to match the server
IP = '0.0.0.0'  # Use '0.0.0.0' to bind to all available interfaces
PORT = 12345  # The port should match the one used by the server

# Initialize a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((IP, PORT))

try:
    print("Starting video stream reception...")
    while True:
        # Receive data from the UDP socket
        packet, _ = sock.recvfrom(65535)  # Buffer size; adjust as needed

        # Reconstruct the frame
        nparr = np.frombuffer(packet, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Display the frame
        cv2.imshow('Video Stream', frame)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Stream reception interrupted by user")

finally:
    sock.close()
    cv2.destroyAllWindows()
    print("Socket closed and OpenCV resources released")
