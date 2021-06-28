import cv2

dog = cv2.imread("../assets/test_dog.jpg")
reisze_dog = cv2.resize(dog, None, fx=0.3, fy=0.3)
flip_dog = cv2.flip(reisze_dog, 0)
flip_dog2 = cv2.flip(reisze_dog, -1)
rotate_dog = cv2.rotate(reisze_dog, cv2.ROTATE_90_CLOCKWISE)
rotate_dog2 = cv2.rotate(reisze_dog, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("dog", dog)
cv2.imshow("reisze_dog", reisze_dog)
cv2.imshow("flip_dog", flip_dog)
cv2.imshow("flip_dog2", flip_dog2)
cv2.imshow("rotate_dog", rotate_dog)
cv2.imshow("rotate_dog2", rotate_dog2)

while True:
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'):
    break

cv2.destroyAllWindows()
