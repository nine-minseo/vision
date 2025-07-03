import cv2
import numpy as np

img = cv2.imread('data/shapes.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

# 그레이스케일 및 이진화 (220 기준)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY_INV)

# 컨투어 검출 (TREE, APPROX_NONE)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

result = img.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 100:  # 너무 작은 노이즈 무시
        continue
    # 꼭지점 근사화 (선이 픽셀 단위로 연결된 경우, 전부 다 꼭지점으로 인식되기 때문에, 근사 해서 꼭지점으로 처리하지 않게 함)
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    x, y, w, h = cv2.boundingRect(approx)
    aspect_ratio = w / h
    # 꼭지점이 12개 이상이면 원으로 간주
    if len(approx) >= 12:
        (cx, cy), radius = cv2.minEnclosingCircle(cnt)
        center = (int(cx), int(cy))
        radius = int(radius)
        cv2.circle(result, center, radius, (0, 255, 255), 2)
        cv2.putText(result, 'Circle', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    elif len(approx) == 5:
        cv2.putText(result, 'Pentagon', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)
        cv2.drawContours(result, [approx], -1, (255, 0, 255), 2)
    elif len(approx) == 10:
        cv2.putText(result, 'Star', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.drawContours(result, [approx], -1, (0, 255, 0), 2)
    elif len(approx) == 4:
        # 사각형/직사각형 판별
        if 0.9 <= aspect_ratio <= 1.1:
            cv2.putText(result, 'Square', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        else:
            cv2.putText(result, 'Rectangle', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.drawContours(result, [approx], -1, (0, 255, 0), 2)
    elif len(approx) == 3:
        cv2.putText(result, 'Triangle', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 128, 255), 2)
        cv2.drawContours(result, [approx], -1, (0, 128, 255), 2)
    else:
        # 기타 도형
        cv2.drawContours(result, [approx], -1, (128, 0, 128), 2)

cv2.imshow('Detected Shapes', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
