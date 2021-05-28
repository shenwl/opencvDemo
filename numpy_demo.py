import cv2
import numpy as np


# ==================创建矩阵=======================
# 一维
a = np.array([1, 2, 3])
# 二维矩阵，2 * 3，也可以更多维，但是大部分时候用二维
b = np.array([[1, 2, 3], [4, 5, 6]])

# (480, 640, 3) 矩阵行个数，列个数，通道数/层数(每个通道代表一个矩阵)
# np.uint8: 矩阵数据类型
c = np.zeros((2, 2, 3), np.uint8)

cc = np.ones((2, 2, 3), np.uint8)
d = np.identity(4)
dd = np.eye(3, 4, k=1)
# print('eye k', dd)

# ==================索引矩阵[y, x] or [y, x, channel]=======================
# img = np.zeros((480, 640, 3), np.uint8)
# print(img[100, 100])
# count = 0
# while count < 200:
#   # y=100画一条200像素蓝色横线
#   # BGR B设为255
#   img[100, count, 0] = 255

#   # y=200画一条200像素绿色横线
#   img[200, count] = [0, 255, 0]

#   count += 1

# cv2.imshow("img_auto_create_window", img)

# key = cv2.waitKey(0)
# if key:
#   cv2.destroyAllWindows()

# ==================提取子矩阵=======================

img2 = np.zeros((480, 640, 3), np.uint8)

# 提取y:100~200, x: 100~200的100*100区域，把它变成红色
roi = img2[100:200, 100:200]
roi[:,:] = [0, 0, 255]
# 把y:10～40,x:10~40区域变绿色
roi[10:40,10:40] = [0, 255, 0]

cv2.imshow("img_roi", roi)

key = cv2.waitKey(0)
if key:
  cv2.destroyAllWindows()