import cv2
import numpy as np

img = cv2.imread("../assets/book.jpeg")

src = np.float32([[200, 3000], [200, 200], [4000, 0], [4000, 2800]])
dst = np.float32([[0, 3000], [0, 0], [4000, 0], [4000, 3000]])
h, w, ch = img.shape

M = cv2.getPerspectiveTransform(src, dst)
dist_img = cv2.warpPerspective(img, M, (w, h))

cv2.imshow('raw', img)
cv2.imshow('dist', dist_img)
while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
