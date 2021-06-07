import cv2
import numpy as np

# 浅拷贝
img1 = cv2.imread('./test.jpg')
img2 = img1

img2[10:100, 10:100] = [0,0,255]

# 深拷贝
img3 = img2.copy()
img3[10:100, 10:100] = [0,255,0]


cv2.imshow("img1", img1) # 有一块红色
cv2.imshow("img2", img2) # 有一块红色
cv2.imshow("img3", img3) # 有一块绿色

key = cv2.waitKey(0)
if key:
  cv2.destroyAllWindows()