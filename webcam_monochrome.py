import cv2  #OpenCV 로드
#print(cv2.__version__)

# 웹캠에서 영상을 읽어서 흑백으로 변환 후 출력
cap = cv2.VideoCapture(0) # 웹캠 사용

if not cap.isOpened():
    print('Error: Cannot open webcam')
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 흑백 변환
        cv2.imshow('video', gray)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()