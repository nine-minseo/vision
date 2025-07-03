import cv2
import numpy as np

# 네 점을 저장할 리스트
clicked_points = []

# 마우스 클릭 콜백 함수
def print_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'클릭 좌표: ({x}, {y})')
        clicked_points.append([x, y])
        if len(clicked_points) == 4:
            cv2.destroyAllWindows()

img = cv2.imread('data/KakaoTalk_tab.jpg')
if img is None:
    print('이미지를 불러올 수 없습니다.')
    exit()

# 원본 이미지를 1/4 크기로 축소
img_small = cv2.resize(img, (img.shape[1]//4, img.shape[0]//4), interpolation=cv2.INTER_AREA)

cv2.imshow('kakao', img_small)
cv2.setMouseCallback('kakao', print_coordinates)

print('이미지 창에서 네 꼭짓점을 차례로 클릭하세요.')
cv2.waitKey(0)
cv2.destroyAllWindows()

if len(clicked_points) == 4:
    # 클릭한 좌표를 원본 이미지 좌표로 환산
    scale_x = img.shape[1] / img_small.shape[1]
    scale_y = img.shape[0] / img_small.shape[0]
    src_pts = np.float32([[x*scale_x, y*scale_y] for x, y in clicked_points])
    width, height = 400, 300  # 원하는 출력 크기
    dst_pts = np.float32([[0,0], [width-1,0], [width-1,height-1], [0,height-1]])
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    warped = cv2.warpPerspective(img, M, (width, height))
    # 결과 이미지를 3배 확대
    warped_big = cv2.resize(warped, (width*3, height*3), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('warped', warped_big)
    print('변환 결과(3배 확대)가 표시됩니다.')
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('네 꼭짓점을 모두 클릭하지 않았습니다.')
