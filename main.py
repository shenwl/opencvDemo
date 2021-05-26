import cv2

# 创建窗口
cv2.namedWindow("test", cv2.WINDOW_NORMAL)
# 显示窗口
cv2.imshow("test", 0)
# 设置窗口大小
cv2.resizeWindow("test", 300, 300)

# 设置窗口展示时间,0为一直展示
key = cv2.waitKey(0)

# 响应推出键盘事件
if key == 'q':
  exit()

cv2.destroyAllWindows()
