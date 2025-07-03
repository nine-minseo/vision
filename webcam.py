import cv2  #OpenCV 로드
#print(cv2.__version__)

# 영상 파일을 읽어서 비디어 객체 cap 생성
cap = cv2.VideoCapture(0) # 웹캠 사용

if not cap.isOpened():
    print('Error: Cannot open video file')
else:
    while True: # 비디오 객체가 열려있는 동안 반복
        ret, frame = cap.read() # 프레임을 읽어오기 / 성공여부, 이미지 객체
        if not ret:
            break
        cv2.imshow('video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'):  # 0.03초 대기 후(영상 출력 후) 'q' 키를 누르면 종료
            break
    cap.release()   # 비디오 객체 해제 (초기화)
    cv2.destroyAllWindows()