import cv2
import numpy as np

img = cv2.imread("../assets/test_dog.jpg")

kernal = np.ones((5, 5), np.float32) / 25

dist = cv2.filter2D(img, -1, kernal)

cv2.imshow('src', img)
cv2.imshow('dist', dist)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
