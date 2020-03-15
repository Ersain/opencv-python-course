import cv2
from skimage import filters

image = cv2.imread('TrinityBikes.JPG', 0)
roberts = filters.roberts(image)
sobel = filters.sobel(image)

cv2.imshow('roberts', roberts)
cv2.imshow('sobel', sobel)

k = cv2.waitKey(0) & 0xFF

if k == '27':
    cv2.destroyAllWindows()
