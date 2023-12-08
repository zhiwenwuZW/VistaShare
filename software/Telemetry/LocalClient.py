from ultralytics import YOLO
import cv2

ip_addr = "127.0.0.1"
port = 8888

model = YOLO('yolov8n.pt')
tcp_addr = f'tcp://{ip_addr}:{port}'

def run_Results():
    # using local ip_addr
    # only keep objects: 2: cars  5: bus 7: truck 9: traffic light 10:fire hydrant 11: stop sign 
    results = model(tcp_addr, stream=True, classes = [0, 2, 5, 7, 9, 10, 11])
    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        

