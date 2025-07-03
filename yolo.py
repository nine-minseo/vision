# Ultralytics YOLO를 이용한 웹캠 실시간 객체 인식 예제 (context7 기반)
# pip install ultralytics 필요
from ultralytics import YOLO
import cv2

# YOLO 모델 로드 (기본 yolov8n.pt, 인터넷 연결 필요)
model = YOLO('yolov8n.pt')

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('웹캠을 열 수 없습니다.')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # YOLO로 추론
    results = model(frame)
    # 결과 시각화
    annotated_frame = results[0].plot()
    cv2.imshow('Ultralytics YOLO Webcam', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
