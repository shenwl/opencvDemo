import cv2

img = cv2.imread('./test.jpg')

# 画一条红线，5px粗细，线型设置不同，16更加平滑，1的锯齿明显
cv2.line(img, (10, 20), (300, 400), (0, 0, 255), 5, 16)
cv2.line(img, (10, 100), (200, 520), (0, 0, 255), 5, 1)

# 画一个左上(100, 100)，右下(200, 200)，绿色填充的矩形(线宽-1)
cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), -1)

# 画一个圆心为(400, 200)，半径为100的蓝色实心圆
cv2.circle(img, (400, 200), 100, (255, 0, 0), -1)
# 画一个同心圆
cv2.circle(img, (400, 200), 20, (0, 0, 255), 5)

cv2.imshow('draw', img)


key = cv2.waitKey(0)
if key:
  cv2.destroyAllWindows()
