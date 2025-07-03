import cv2

# 얼굴 검출기 로드
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# 웹캠 사용
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('웹캠을 열 수 없습니다.')
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    for (x, y, w, h) in faces:
        # 얼굴 영역 모자이크 처리
        face_roi = frame[y:y+h, x:x+w]
        if face_roi.size > 0:
            mosaic = cv2.resize(face_roi, (16, 16), interpolation=cv2.INTER_LINEAR)
            mosaic = cv2.resize(mosaic, (w, h), interpolation=cv2.INTER_NEAREST)
            frame[y:y+h, x:x+w] = mosaic
    cv2.imshow('Webcam Face Mosaic', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
