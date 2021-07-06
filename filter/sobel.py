import cv2
import numpy as np

img = cv2.imread("../assets/cat.jpg")
src = cv2.resize(img, None, fx=0.2, fy=0.2)

# 索贝尔算子y方向边缘
d1 = cv2.Sobel(src, cv2.CV_64F, 1, 0, ksize=3)
# 索贝尔算子x方向边缘
d2 = cv2.Sobel(src, cv2.CV_64F, 0, 1, ksize=3)

dst = d1 + d2

cv2.imshow('src', src)
cv2.imshow('y edge', d1)
cv2.imshow('x edge', d2)
cv2.imshow('add dx, dy', dst)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
