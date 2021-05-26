import cv2

cv2.namedWindow("videoread", cv2.WINDOW_NORMAL)

cap = cv2.VideoCapture(0)

while True:
  # 从摄像头读取视频帧
  ret, frame = cap.read()

  cv2.imshow("videoread", frame)

  key = cv2.waitKey(5)
  if key & 0xff == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
