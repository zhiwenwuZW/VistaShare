import cv2
import socket
import numpy as np
import threading

# Function to handle each stream
def receive_stream(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', port))

    cv2.namedWindow(str(port))  # Create a window for each stream

    try:
        while True:
            packet, _ = sock.recvfrom(65535)  # Adjust buffer size as needed
            nparr = np.frombuffer(packet, np.uint8)
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

            if frame is not None:
                cv2.imshow(str(port), frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        sock.close()
        cv2.destroyWindow(str(port))

# Ports for the two Raspberry Pi streams
ports = [12345, 12346]

# Create and start threads for each stream
threads = []
for port in ports:
    thread = threading.Thread(target=receive_stream, args=(port,))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

cv2.destroyAllWindows()
print("All streams closed.")
