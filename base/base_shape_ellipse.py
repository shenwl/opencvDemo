import cv2

img = cv2.imread('./test.jpg')

# 度是按顺时针计算的
# 0度是从左侧开始的
cv2.ellipse(img, (400, 400), (200, 100), 0, 0, 360, (0, 0, 255))
# 填充
cv2.ellipse(img, (400, 400), (200, 100), 0, 0, 360, (0, 0, 255), -1)

cv2.imshow('draw', img)


key = cv2.waitKey(0)
if key:
  cv2.destroyAllWindows()
