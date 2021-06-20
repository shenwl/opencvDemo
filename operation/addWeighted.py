import cv2

pika = cv2.imread("./test.jpg")
bg = cv2.imread("./test2.jpg")

result = cv2.addWeighted(pika, 0.7, bg, 0.3, 0)

cv2.imshow("pika", pika)
cv2.imshow("bg", bg)
cv2.imshow("result", result)

while True:
  key = cv2.waitKey(1) & 0xff

  if key == ord('q'):
    break

cv2.destroyAllWindows()
