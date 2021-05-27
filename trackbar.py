import cv2
import numpy as np

WIN_NAME = "trackbar_test_window"
TRACKBAR_NAME_R = "trackbar_name_R"
TRACKBAR_NAME_G = "trackbar_name_G"
TRACKBAR_NAME_B = "trackbar_name_B"

cv2.namedWindow(WIN_NAME, cv2.WINDOW_NORMAL)


def callback():
  pass


cv2.createTrackbar(TRACKBAR_NAME_R, WIN_NAME, 0, 255, callback)
cv2.createTrackbar(TRACKBAR_NAME_G, WIN_NAME, 0, 255, callback)
cv2.createTrackbar(TRACKBAR_NAME_B, WIN_NAME, 0, 255, callback)

img = np.zeros((480, 460, 3), np.uint8)

while True:
  cv2.imshow(WIN_NAME, img)

  r = cv2.getTrackbarPos(TRACKBAR_NAME_R, WIN_NAME)
  g = cv2.getTrackbarPos(TRACKBAR_NAME_G, WIN_NAME)
  b = cv2.getTrackbarPos(TRACKBAR_NAME_B, WIN_NAME)

  img[:] = [b, g, r]

  key = cv2.waitKey(10)
  if key & 0xff == ord('q'):
    break

cv2.destroyAllWindows()
