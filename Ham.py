import cv2
import os

path =  r'C:\Users\Phong Nguyen\Pictures\Green-Laptop-Wallpapers.jpg'
path1 = r'C:\Users\Phong Nguyen\Pictures'
img = cv2.imread(path)
cv2.imshow('tai anh', img)


os.chdir(path1)

fileName = 'anh moi.png'
cv2.imwrite(fileName,img)

print('thanh cong')
cv2.waitKey()