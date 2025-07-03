# Ultralytics YOLO + OpenCV + matplotlib + BOT-SORT 트래킹 기반 자동차 카운팅 (유튜브 영상 스트리밍 지원)
# pip install ultralytics opencv-python matplotlib yt-dlp 필요
from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# 유튜브 mp4 스트림 URL 얻기
def get_youtube_stream_url(youtube_url):
    import yt_dlp
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'quiet': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        return info['url']

# 유튜브 영상 링크
youtube_url = "https://www.youtube.com/watch?v=3lnHHDQ1v5E"
video_path = get_youtube_stream_url(youtube_url)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print('유튜브 영상을 열 수 없습니다.')
    exit()

model = YOLO('yolov8n.pt')
car_class_names = ['car', 'truck', 'bus']

car_counts = []
frame_idx = 0
unique_ids = set()

plt.ion()
fig, ax = plt.subplots()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # BOT-SORT 트래킹 사용
    results = model.track(frame, persist=True, tracker="botsort.yaml")
    boxes = results[0].boxes
    count = 0
    ids_in_frame = set()

    for box in boxes:
        cls = int(box.cls[0])
        label = model.model.names[cls]
        if label in car_class_names:
            # 트래킹 ID 추출
            if hasattr(box, 'id') and box.id is not None:
                track_id = int(box.id[0])
                ids_in_frame.add(track_id)
            count += 1

    # 전체 유니크 자동차 ID 집합에 추가
    unique_ids.update(ids_in_frame)
    car_counts.append(len(unique_ids))
    frame_idx += 1

    # 시각화
    annotated = results[0].plot()
    cv2.imshow('Car Tracking', annotated)

    # 실시간 그래프 업데이트
    ax.clear()
    ax.plot(car_counts, label='Unique Car Count')
    ax.set_xlabel('Frame')
    ax.set_ylabel('Unique Cars')
    ax.set_title('Unique Car Count Over Time')
    ax.legend()
    plt.pause(0.001)

    # ESC로 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
plt.ioff()