import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera can't be opened")
else:
    ret, frame = cap.read()
    if ret:
        print("Frame captured")
        # Optionally display the frame using cv2.imshow()
    else:
        print("Failed to capture frame")

cap.release()
