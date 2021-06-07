import cv2
import numpy as np

img = cv2.imread('./test.jpg')

# 图像的尺寸和通道数
print(img.shape) # (960, 1280, 3)
# 大小
print(img.size) # 3686400 = 960*1280*3
# 图像中的每个元素的位深
print(img.dtype) # uint8