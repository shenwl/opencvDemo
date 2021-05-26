import cv2

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# 分辨率按摄像头真实分辨率设置，不然可能保存不成功
videoWriter = cv2.VideoWriter("./temp/test_video_writer.mp4", fourcc, 25, (1280, 720))

cv2.namedWindow("videoread", cv2.WINDOW_NORMAL)
cap = cv2.VideoCapture(0)

# 判断摄像头状态
while cap.isOpened():
  ret, frame = cap.read()

  if ret == True:
    cv2.imshow("videoread", frame)
    # 窗口可能被内容撑大，这里resize一下
    cv2.resizeWindow("videoread", 640, 360)

    # 写帧
    videoWriter.write(frame)

    # 设置40ms读取一次, 25fps
    key = cv2.waitKey(40)
    if key & 0xff == ord('q'):
      break
  else:
    break

cap.release()
videoWriter.release()
cv2.destroyAllWindows()
