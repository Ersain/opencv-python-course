import cv2

img = cv2.imread('labka.jpg')
blur = cv2.blur(img, (20, 20))

cv2.imshow('original', img)
cv2.imshow('blurred image', blur)

key = cv2.waitKey(0) & 0xFF

if key == '27':
    cv2.destroyAllWindows()
