import cv2
import numpy as np

img = cv2.imread('./test.jpg')

pts = np.array([(300, 10), (150, 100), (450, 100), (500, 300)], np.int32)
cv2.polylines(img, [pts], True, (0, 0, 255))
# 填充三角形
pts2 = np.array([(300, 200), (150, 300), (450, 300)], np.int32)
cv2.fillPoly(img, [pts2], (0, 255, 0))

cv2.imshow('draw', img)

key = cv2.waitKey(0)
if key:
  cv2.destroyAllWindows()
