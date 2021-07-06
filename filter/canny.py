import cv2

src = cv2.imread("../assets/tom.jpeg")
# src = cv2.resize(img, None, fx=0.2, fy=0.2)

dst = cv2.Canny(src, 50, 100)

cv2.imshow('src', src)
cv2.imshow('canny', dst)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
