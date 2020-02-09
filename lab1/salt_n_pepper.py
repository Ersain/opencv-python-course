import random

import cv2
import numpy as np


def salt_n_pepper(image, prob):
    result = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                result[i][j] = 0
            elif rdn > thres:
                result[i][j] = 255
            else:
                result[i][j] = image[i][j]
    return result


img = cv2.imread('labka.jpg', 0)
noise_img = salt_n_pepper(img, 0.05)

cv2.imshow('original', img)
cv2.imshow('salt and pepper noise', noise_img)

cv2.randu()

k = cv2.waitKey(0) & 0xFF

if k == '27':
    cv2.destroyAllWindows()
