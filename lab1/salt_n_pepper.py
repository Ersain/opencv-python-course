import random

import cv2
import numpy as np

img = cv2.imread('labka.jpg')

result = np.zeros(img.shape, np.uint8)
prob = 0.2
edge = 1 - prob

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        rdn = random.random()
        if rdn < prob:
            result[i][j] = 0
        elif rdn > edge:
            result[i][j] = 255
        else:
            result[i][j] = img[i][j]

cv2.imshow('original', img)
cv2.imshow('salt and pepper noise', result)

cv2.imwrite('salt_n_pepper.jpg', result)

k = cv2.waitKey(0) & 0xFF

if k == '27':
    cv2.destroyAllWindows()
