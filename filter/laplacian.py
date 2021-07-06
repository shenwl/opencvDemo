import cv2

img = cv2.imread("../assets/cat.jpg")
src = cv2.resize(img, None, fx=0.2, fy=0.2)

dst = cv2.Laplacian(src, cv2.CV_64F)

cv2.imshow('src', src)
cv2.imshow('Laplacian dst', dst)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
