import cv2

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
img_mat = cv2.imread('./test.jpg')

cv2.imshow("img", img_mat)

key = cv2.waitKey(0)

if key & 0xff == ord('q'):
  exit()

cv2.destroyAllWindows()
