import cv2
import numpy as np

# 500x500 하얀색 배경 이미지 생성
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# 파란색 직선 그리기
cv2.line(img, (50, 50), (450, 50), (255, 0, 0), 5)

# 초록색 사각형 그리기
cv2.rectangle(img, (50, 100), (200, 250), (0, 255, 0), 3)

# 빨간색 원 그리기
cv2.circle(img, (350, 175), 60, (0, 0, 255), -1)

# 보라색 타원 그리기
cv2.ellipse(img, (250, 400), (100, 50), 0, 0, 180, (255, 0, 255), 2)

# 검정색 다각형 그리기
pts = np.array([[300,300],[400,350],[350,450],[250,450],[200,350]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], isClosed=True, color=(0,0,0), thickness=3)

# 텍스트 쓰기
cv2.putText(img, 'OpenCV Drawing', (70, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, (128, 0, 128), 2, cv2.LINE_AA)

# 이미지 보여주기
cv2.imshow('Drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
