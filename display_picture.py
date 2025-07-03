import cv2  #OpenCV 로드
#print(cv2.__version__)


img = cv2.imread('data/Dog.jpg')
# 이 파일과 같은 경로에 있는 data folder
# 안에 dog.jpg를 읽어서 OpenCV 객체
# img로 저장
cv2.imshow("img", img)
# img 객체를 img 이름을 가진 새창에 띄움
cv2.waitKey(10000)
# 인수값 만큼 기다리거나(창의 띄움) (인수 없음면 무한대)
# 키보드 입력이 있을때까지 기다리기
cv2.destroyAllWindows()
# 모든 새창 끄기