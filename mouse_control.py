import cv2
import numpy as np


def mouse_callback(evt, x, y, flags, userdata):
  print(evt, x, y, flags, userdata)


win_name = "mouse_windows"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win_name, 640, 360)

cv2.setMouseCallback(win_name, mouse_callback, "=======")

# 640 * 360的黑图
img = np.zeros((360, 640, 3), np.uint8)
while True:
  cv2.imshow(win_name, img)
  key = cv2.waitKey(1)
  if key & 0xff == ord('q'):
    break
cv2.destroyAllWindows()
