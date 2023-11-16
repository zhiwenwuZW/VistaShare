import cv2
import socket
import numpy as np

# Server's IP and PORT
SERVER_IP = '192.168.10.228'
SERVER_PORT = 5555

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.bind((SERVER_IP, SERVER_PORT))

print("Client Start Receive Video")

try:
    while True:
        # Receive data
        packet, _ = client_socket.recvfrom(65536)  # Adjust buffer size as needed

        # Convert packet data to image
        npimg = np.frombuffer(packet, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)

        # Display the image
        cv2.imshow("Stream", source)

        # Save the current frame as image.jpg
        cv2.imwrite('image.jpg', source)

        # Break loop with a key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Close the socket and release resources
    client_socket.close()
    cv2.destroyAllWindows()
    print("Client resources have been freed.")
