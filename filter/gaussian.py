import cv2

img = cv2.imread("../assets/cat.jpg")
src = cv2.resize(img, None, fx=0.2, fy=0.2)

dst = cv2.GaussianBlur(src, (3, 3), sigmaX=1)
dst2 = cv2.GaussianBlur(src, (7, 7), sigmaX=1)

cv2.imshow('src', src)
cv2.imshow('blur3*3', dst)
cv2.imshow('blur7*7', dst2)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
