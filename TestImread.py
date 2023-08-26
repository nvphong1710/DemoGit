import cv2

path = r'C:\Users\Phong Nguyen\Pictures\Green-Laptop-Wallpapers.jpg'

# Đọc hình ảnh
image = cv2.imread(path)

# Kiểm tra xem hình ảnh đã được đọc thành công chưa
if image is not None:
    # Thực hiện các thao tác xử lý ảnh ở đây
    cv2.imshow('Image', image)  # Hiển thị hình ảnh
    cv2.waitKey(0)              # Chờ người dùng đóng cửa sổ
    cv2.destroyAllWindows()     # Đóng cửa sổ
else:
    print("Không thể đọc hình ảnh")
