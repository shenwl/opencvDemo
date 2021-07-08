import cv2

img = cv2.imread("../assets/book.jpeg")
src = cv2.resize(img, None, fx=0.2, fy=0.2)

gray_img = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, dst = cv2.threshold(gray_img, 100, 255, cv2.THRESH_BINARY)
dst_adaptive = cv2.adaptiveThreshold(
  gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
  cv2.THRESH_BINARY, 5, 0
)

cv2.imshow('src', src)
cv2.imshow('threshold bin', dst)
cv2.imshow('adaptive bin', dst_adaptive)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
