import cv2
import numpy as np

img = cv2.imread('../labka.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_labka.jpg', img_gray)

img_gray = cv2.imread('grayscale_labka.jpg')

z = img_gray.reshape((-1, 3))

z = np.float32(z)
crit = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
k = 6
ret, label, center = cv2.kmeans(z, k, None, crit, 10, cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape(img_gray.shape)

cv2.imshow('res2', res2)
key = cv2.waitKey(0) & 0xFF

if key == '27':
    cv2.destroyAllWindows()
