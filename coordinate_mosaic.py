import cv2

# 마우스 클릭 콜백 함수
def print_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'클릭 좌표: ({x}, {y})')

img = cv2.imread('data/car.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

# (782, 167), (122, 550) 두 좌표 기준으로 모자이크 처리
x1, y1 = 122, 167
x2, y2 = 782, 550
# 좌상단, 우하단 정렬
x_min, x_max = min(x1, x2), max(x1, x2)
y_min, y_max = min(y1, y2), max(y1, y2)

roi = img[y_min:y_max, x_min:x_max]
if roi.size > 0:
    mosaic = cv2.resize(roi, (20, 20), interpolation=cv2.INTER_LINEAR)
    mosaic = cv2.resize(mosaic, (x_max-x_min, y_max-y_min), interpolation=cv2.INTER_NEAREST)
    img[y_min:y_max, x_min:x_max] = mosaic

cv2.imshow('car_mosaic', img)
cv2.setMouseCallback('car_mosaic', print_coordinates)

print('이미지 창에서 마우스로 클릭하면 좌표가 출력됩니다. (모자이크 영역 확인)')
cv2.waitKey(0)
cv2.destroyAllWindows()
