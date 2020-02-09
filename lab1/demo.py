import cv2

img = cv2.imread('labka.jpg')

cv2.imshow('original', img)

k = cv2.waitKey(0) & 0xFF

if k == '27':
    cv2.destroyAllWindows()
