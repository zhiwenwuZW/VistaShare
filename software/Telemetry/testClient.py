from ultralytics import YOLO
import cv2

model = YOLO('yolov8n.pt')
results = model('tcp://192.168.52.228:8888', stream=True)

for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions

    cv2.imshow('YOLO Detection', im_array)
    
    # Wait for a key press and break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
