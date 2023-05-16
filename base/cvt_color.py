import cv2

WIN_NAME = "color_window"
TRACKBAR_NAME = "current_color"

# 定义在modules/imgproc/include/opencv2/imgproc.hpp
color_spaces = [
  cv2.COLOR_BGR2BGRA, cv2.COLOR_BGR2RGBA,
  cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV_FULL,
  cv2.COLOR_BGR2YUV,
]

cv2.namedWindow(WIN_NAME, cv2.WINDOW_NORMAL)

def callback():
  pass


img = cv2.imread("./test.jpg")

cv2.createTrackbar(TRACKBAR_NAME, WIN_NAME, 0, len(color_spaces) - 1, callback)

while True:
  cur_color_space = color_spaces[cv2.getTrackbarPos(TRACKBAR_NAME, WIN_NAME)]

  # 转换色彩空间
  cvt_img = cv2.cvtColor(img, cur_color_space)
  print('cur_color_space: ', cur_color_space)

  cv2.imshow(WIN_NAME, cvt_img)

  key = cv2.waitKey(10)
  if key & 0xff == ord('q'):
    break

cv2.destroyAllWindows()
