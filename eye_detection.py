import cv2

# 눈 검출기 로드
eye_cascade = cv2.CascadeClassifier('data/haarcascade_eye.xml')

# 이미지 읽기
img = cv2.imread('data/lena.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 눈 검출
# (얼굴 전체에서 눈을 찾음)
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

# 눈 영역 표시
for (x, y, w, h) in eyes:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

print(f'검출된 눈 수: {len(eyes)}')
cv2.imshow('Eye Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
