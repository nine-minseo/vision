import cv2

# 얼굴 검출기 로드
face_cascade = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# 이미지 읽기
img = cv2.imread('data/lena.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 얼굴 검출
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# 얼굴 영역 표시
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

print(f'검출된 얼굴 수: {len(faces)}')
cv2.imshow('Face Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
