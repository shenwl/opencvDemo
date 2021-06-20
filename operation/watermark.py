"""
给图片添加水印
1. 创建logo
2. 引入图片
3. 给图片添加水印
  - 计算图片在什么地方添加，在添加的地方变成纯黑色
  - 利用add，将logo与图片叠加到一起
4. 输出新图片
"""
import cv2
import numpy as np

raw = cv2.imread('./test.jpg')
rect_logo = np.zeros((200, 200, 3), np.uint8)
mask = np.zeros((200, 200), np.uint8)

rect_logo[20:120, 20:120] = [0, 0, 255]
rect_logo[80:180, 80:180] = [255, 0, 0]

mask[20:120, 20:120] = 255
mask[80:180, 80:180] = 255

mask = cv2.bitwise_not(mask)

# 选择添加logo的位置
roi = raw[0:200, 0:200]

tmp = cv2.bitwise_and(roi, roi, mask=mask)
dist = cv2.add(tmp, rect_logo)
raw[0:200, 0:200] = dist

cv2.imshow('logo', rect_logo)
cv2.imshow('mask', mask)
cv2.imshow('tmp', tmp)
cv2.imshow('dist', dist)
cv2.imshow('raw', raw)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
