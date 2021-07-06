import cv2

src = cv2.imread("../assets/tom.jpeg")

dst = cv2.bilateralFilter(src, 7, 20, 50)

cv2.imshow('src', src)
cv2.imshow('blur', dst)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
