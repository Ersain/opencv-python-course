import cv2
import numpy as np

img = cv2.imread('labka.jpg')

gauss = np.zeros(img.shape, np.uint8)
mean = (0, 0, 0)
sigma = (50, 50, 50)
cv2.randn(gauss, mean, sigma)

modified_img = cv2.add(img, gauss)
cv2.imwrite('gaussian_noise.jpg', modified_img)

cv2.imshow('original', img)
cv2.imshow('gaussian noise', modified_img)

key = cv2.waitKey(0) & 0xFF

if key == '27':  # This is Escape button
    cv2.destroyAllWindows()
