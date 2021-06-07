import cv2

img = cv2.imread('./test.jpg')

cv2.putText(img, "HelloWorld", (400, 200), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0))

cv2.imshow('draw', img)

key = cv2.waitKey(0)
if key:
  cv2.destroyAllWindows()
