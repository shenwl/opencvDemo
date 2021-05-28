import cv2
import numpy as np

# 浅拷贝
img1 = cv2.imread('./test.jpg')
img2 = img1

img2[10:100, 10:100] = [0,0,255]

cv2.imshow("img1", img1)

key = cv2.waitKey(0)
if key:
  cv2.destroyAllWindows()