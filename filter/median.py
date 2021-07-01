import cv2

src = cv2.imread("../assets/pepper.png")

dst = cv2.medianBlur(src, 3)
dst2 = cv2.medianBlur(src, 7)

cv2.imshow('src', src)
cv2.imshow('blur ksize=3', dst)
cv2.imshow('blur ksize=7', dst2)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
