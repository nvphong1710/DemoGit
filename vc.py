import cv2

video = r'C:\Users\Phong Nguyen\Downloads\SnapSave.io-Cảnh biển đẹp _ Beautiful Beach - Hd 1080p.mp4'

# Tạo đối tượng VideoCapture
cap = cv2.VideoCapture (video)

# Kiểm tra xem nguồn đã mở thành công hay chưa
if not cap.isOpened():
    print("Không thể mở nguồn đầu vào")
    exit()

while True:
    ret, frame = cap.read()  # Đọc khung hình

    if not ret:
        print("Không thể đọc khung hình")
        break

    cv2.imshow('Frame', frame)  # Hiển thị khung hình

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # Giải phóng tài nguyên
cv2.destroyAllWindows()  # Đóng cửa sổ