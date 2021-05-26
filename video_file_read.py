import cv2
cv2.namedWindow("videoread", cv2.WINDOW_NORMAL)

# 从视频文件读取
cap = cv2.VideoCapture("./test_video.mp4")

while True:
  ret, frame = cap.read()
  cv2.imshow("videoread", frame)

  # 设置40ms读取一次, 25fps
  key = cv2.waitKey(40)
  if key & 0xff == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()
