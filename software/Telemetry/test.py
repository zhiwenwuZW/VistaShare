from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model('tcp://127.0.0.1:8888', stream=True)