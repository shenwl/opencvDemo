"""
基本绘画功能
1. 画线：按下l键拖动鼠标
2. 画矩形: 按下r键拖动鼠标
3. 画圆: 按下c键拖动鼠标
"""
import cv2
import numpy as np
from mouse_canvas.canvas_shapes import CanvasShapes
from math import sqrt

current_shape = None
startpos = (0, 0)

img = np.zeros((480, 640, 3), np.uint8)


def mouse_callback(evt, x, y, flags, userdata):
  global startpos
  if evt & cv2.EVENT_LBUTTONDOWN == cv2.EVENT_LBUTTONDOWN:
    startpos = (x, y)
  elif evt & cv2.EVENT_LBUTTONUP == cv2.EVENT_LBUTTONUP:
    if current_shape == CanvasShapes.LINE:
      cv2.line(img, startpos, (x, y), (0, 0, 255))
    elif current_shape == CanvasShapes.RECT:
      cv2.rectangle(img, startpos, (x, y), (0, 0, 255))
    elif current_shape == CanvasShapes.CIRCLE:
      center = startpos
      r = int(sqrt((x - startpos[0]) ** 2 + (y - startpos[1]) ** 2))
      cv2.circle(img, center, r, (0, 0, 255))


win_name = "mouse_draw_windows"
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(win_name, 640, 360)

cv2.setMouseCallback(win_name, mouse_callback)

while True:
  cv2.imshow(win_name, img)
  key = cv2.waitKey(1) & 0xff

  if key == ord('q'):
    break

  if key == ord('l'):
    current_shape = CanvasShapes.LINE
  if key == ord('r'):
    current_shape = CanvasShapes.RECT
  if key == ord('c'):
    current_shape = CanvasShapes.CIRCLE

cv2.destroyAllWindows()
