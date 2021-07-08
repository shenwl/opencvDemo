import cv2
import numpy as np

img = cv2.imread("../assets/cat.jpg")
src = cv2.resize(img, None, fx=0.2, fy=0.2)

gray_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, bin_img = cv2.threshold(gray_img, 180, 255, cv2.THRESH_BINARY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dst = cv2.erode(bin_img, kernel, iterations=1)

cv2.imshow('src', src)
cv2.imshow('bin', bin_img)
cv2.imshow('dst', dst)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
