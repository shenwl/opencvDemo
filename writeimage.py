import cv2

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
img_mat = cv2.imread('./test.jpg')
cv2.imshow("img", img_mat)

key = cv2.waitKey(0)

while True:
  if key & 0xff == ord('q'):
    break
  elif key & 0xff == ord('s'):
    # bool imwrite( constString& filename, InputArrayimg, conststd::vector<int>& params = std::vector<int>());
    cv2.imwrite('./temp/test-write.png', img_mat)
    break

cv2.destroyAllWindows()

