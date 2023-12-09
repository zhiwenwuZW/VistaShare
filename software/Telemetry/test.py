import cv2
import sys
from ultralytics import YOLO
# from ultralytics import RTDETR

IP = "192.168.52.64"
IP2 = "192.168.52.225"
PORT = 8888
PORT2 = 8889

stream_address = f"tcp://{IP}:{PORT}" 
stream_address2 = f"tcp://{IP2}:{PORT2}"

# Open a connection to the video stream
cap = cv2.VideoCapture(stream_address)
cap2 = cv2.VideoCapture(stream_address2)

# Initiate YOLO model
model = YOLO('yolov8n.pt')
model2 = YOLO('yolov8n.pt')
model.conf = 0.8
model2.conf = 0.8

# Initiate Cut Border
cut_x1 = 0
cut_x2 = 0
cut_y1 = 0
cut_y2 = 0
xyxy = []
xyxy2 = []

if not cap.isOpened():
    print("Cannot open stream")
    sys.exit()
if not cap2.isOpened():
    print("Cannot open stream2")
    sys.exit()

while True:
    # Receive Frame
    ret, frame = cap.read()    
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    ret2, frame2 = cap2.read()
    if not ret2: 
        print("Can't receive frame : 2 (stream end?). Exiting ...")


    # only keep objects: 0: human 2: cars  5: bus 7: truck 9: traffic light 10:fire hydrant 11: stop sign 
    results = model(frame, stream=True, classes = [0, 2, 5, 7, 9, 10, 11])  # predict on an image
    results2 = model(frame2, stream=True, classes = [0, 5, 7, 9, 10, 11])

    # Deal with Cam1
    for result in results:
        boxes = result.boxes
        ids = boxes.id
        xyxy = boxes.xyxy

        # Calculate the center of image
        img_center_x = result.orig_shape[1] / 2
        img_center_y = result.orig_shape[0] *2 / 3

        for box in xyxy:
            x1, y1, x2, y2 = box
            if x1 <= img_center_x <= x2 and y1 <= img_center_y <= y2:
                cut_x1, cut_x2, cut_y1, cut_y2 = x1, x2, y1, y2

        print(f"Cut edge {cut_x1} {cut_x2} {cut_y1} {cut_y2}")
        # Display the resulting frame
        plotted_frame = result.plot()
        cv2.imshow('Frame', plotted_frame)

    # Deal with Cam2
    for result2 in results2:
        boxes2 = result2.boxes
        ids2 = boxes2.id
        xyxy2 = boxes2.xyxy

        plotted_frame2 = result2.plot()
        cv2.imshow('Frame2', plotted_frame2)

    roi = frame[int(cut_y1):int(cut_y2), int(cut_x1):int(cut_x2)]
    start_x = cut_x1
    start_y = cut_y1
    end_y = start_y + roi.shape[0]
    end_x = start_x + roi.shape[1]

    if end_y <= frame2.shape[0] and end_x <= frame2.shape[1]:
        frame2[start_y:end_y, start_x:end_x] = roi

    cv2.imshow('Edited', frame2)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()




