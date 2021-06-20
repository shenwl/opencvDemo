import cv2
import numpy as np

# shape: (height, width, channels)
pic_img = cv2.imread("./test.jpg")
mask_img = np.ones(pic_img.shape, np.uint8) * 30
mask_img2 = np.ones(pic_img.shape, np.uint8) * 5

add_img = cv2.add(pic_img, mask_img)
subtract_img = cv2.subtract(pic_img, mask_img)
multiply_img = cv2.multiply(pic_img, mask_img2)
divide_img = cv2.divide(pic_img, mask_img2)

cv2.imshow("before", pic_img)
cv2.imshow("add", add_img)
cv2.imshow("subtract", subtract_img)
cv2.imshow("multiply", multiply_img)
cv2.imshow("divide", divide_img)

while True:
  key = cv2.waitKey(1) & 0xff

  if key == ord('q'):
    break

cv2.destroyAllWindows()
