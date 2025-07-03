import cv2

# 이미지 읽기
img = cv2.imread('data/car.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

# 1. 크기 절반으로 축소
img_half = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv2.INTER_AREA)
cv2.imwrite('data/car_half.jpg', img_half)

# 2. 크기 2배로 확대
img_double = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2), interpolation=cv2.INTER_CUBIC)
cv2.imwrite('data/car_double.jpg', img_double)

# 3. 300x100으로 비율 무시하고 변환
img_300x100 = cv2.resize(img, (300, 100), interpolation=cv2.INTER_LINEAR)
cv2.imwrite('data/car_300x100.jpg', img_300x100)

# 4. 가로만 2배, 세로는 그대로
img_w2 = cv2.resize(img, (img.shape[1]*2, img.shape[0]), interpolation=cv2.INTER_LINEAR)
cv2.imwrite('data/car_w2.jpg', img_w2)

# 5. 세로만 2배, 가로는 그대로
img_h2 = cv2.resize(img, (img.shape[1], img.shape[0]*2), interpolation=cv2.INTER_LINEAR)
cv2.imwrite('data/car_h2.jpg', img_h2)

print('다양한 사이즈 변환 이미지가 data 폴더에 저장되었습니다.')
