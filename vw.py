import cv2

video = r'C:\Users\Phong Nguyen\Downloads\SnapSave.io-Cảnh biển đẹp _ Beautiful Beach - Hd 1080p.mp4'

# Tạo đối tượng VideoCapture
cap = cv2.VideoCapture(video)

# Tạo đối tượng VideoWriter
output_filename = 'video_xuli'
codec = cv2.VideoWriter_fourcc(*'XVID')
fps = 30
frame_size = (640, 480)
out = cv2.VideoWriter(output_filename, codec, fps, frame_size)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Xử lý khung hình (nếu cần)

    out.write(frame)  # Ghi khung hình vào tệp video

cap.release()  # Giải phóng tài nguyên
out.release()  # Đóng tệp video
cv2.destroyAllWindows()