import cv2
import numpy as np

img = np.ones([200, 200], np.uint8)
img2 = np.ones([200, 200], np.uint8)

img[50:150, 50:150] = 255
img2[80:180, 80:180] = 255

img_not = cv2.bitwise_not(img)
img_and = cv2.bitwise_and(img, img2)
img_or = cv2.bitwise_or(img, img2)
img_xor = cv2.bitwise_xor(img, img2)

cv2.imshow("img", img)
cv2.imshow("img2", img2)
# cv2.imshow("img_not", img_not)
# cv2.imshow("img_and", img_and)
# cv2.imshow("img_or", img_or)
cv2.imshow("img_xor", img_xor)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
