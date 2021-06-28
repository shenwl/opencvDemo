import cv2

img = cv2.imread("../assets/test_dog.jpg")
src = cv2.resize(img, None, fx=0.3, fy=0.3)

dist_blur = cv2.blur(src, (5, 5))
dist_box = cv2.boxFilter(src, -1, (5, 5))

cv2.imshow('src', src)
cv2.imshow('blur', dist_blur)
cv2.imshow('box', dist_box)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
