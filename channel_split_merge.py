import cv2
import numpy as np

img = cv2.imread('./test.jpg')

b, g, r = cv2.split(img)

b[10:200, 10:200] = 255
g[10:200, 10:200] = 255

cv2.imshow('img', img)
cv2.imshow('b', b)
cv2.imshow('g', g)

img2 = cv2.merge((b, g, r))

cv2.imshow('img2', img2)

key = cv2.waitKey(0)
if key:
  cv2.destroyAllWindows()