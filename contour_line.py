import cv2
import numpy as np

# 이미지 읽기
img = cv2.imread('data/opencv-logo.png')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

# 그레이스케일 변환 및 이진화
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh = cv2.threshold(gray, 70, 255, 0)

# 등고선 찾기
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 등고선 그리기
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (225,255,225), 2)   # RGB가 아니라 BGR 순서로 색상 지정함

# 등고선 개수와 넓이 출력
print(f'등고선 개수: {len(contours)}')
for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    print(f'등고선 {i+1} 넓이: {area}')

cv2.imshow('Contours', contour_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
