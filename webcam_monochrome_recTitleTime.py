import cv2  #OpenCV 로드
import datetime
#print(cv2.__version__)

# 웹캠에서 영상을 읽어서 흑백으로 변환 후 출력
cap = cv2.VideoCapture(0) # 웹캠 사용

rec_visible = True  # REC 깜빡임 상태
rec_timer = 0       # 프레임 카운터

if not cap.isOpened():
    print('Error: Cannot open webcam')
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 흑백 변환
        # 컬러로 변환 (텍스트, 도형 표시를 위해)
        display = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        # 왼쪽 상단 빨간 점 먼저, 그 다음에 REC 텍스트
        if rec_visible:
            cv2.circle(display, (35, 25), 8, (0,0,255), -1)  # 점 먼저
            cv2.putText(display, 'REC', (50, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA)  # 텍스트
        rec_timer += 1
        if rec_timer % 30 == 0:
            rec_visible = not rec_visible

        # 오른쪽 상단 제목과 현재 시간
        title = 'CCTV Camera'
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        (w, h), _ = cv2.getTextSize(title, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
        cv2.putText(display, title, (display.shape[1]-w-15, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2, cv2.LINE_AA)
        (w2, h2), _ = cv2.getTextSize(now, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
        cv2.putText(display, now, (display.shape[1]-w2-15, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2, cv2.LINE_AA)

        cv2.imshow('video', display)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()