import cv2
import numpy as np

dog = cv2.imread("../assets/test_dog.jpg")
reiszed_dog = cv2.resize(dog, None, fx=0.5, fy=0.5)
h, w, ch = reiszed_dog.shape

"""
方法1：获取旋转矩阵
"""
# M = cv2.getRotationMatrix2D((w/2, h/2), 15, 0.3)

"""
方法2：通过三个点的变化确定变换矩阵
"""
src = np.float32(
  [[100, 50], [200, 50], [100, 150]],
)
dst = np.float32(
  [[150, 120], [220, 80], [80, 100]],
)
M = cv2.getAffineTransform(src, dst)

# 如果想修改dist图像的尺寸，需要修改dsize
dist = cv2.warpAffine(reiszed_dog, M, (int(w/2), int(h/2)))

cv2.imshow('dist', dist)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
