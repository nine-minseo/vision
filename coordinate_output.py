import cv2

# 마우스 클릭 콜백 함수
def print_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'클릭 좌표: ({x}, {y})')

img = cv2.imread('data/car.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

cv2.imshow('car', img)
cv2.setMouseCallback('car', print_coordinates)

print('이미지 창에서 마우스로 클릭하면 좌표가 출력됩니다.')
cv2.waitKey(0)
cv2.destroyAllWindows()
