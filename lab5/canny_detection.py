import cv2 as cv

img = cv.imread('TrinityBikes.jpg', 0)
edges = cv.Canny(img, 100, 200)

cv.imshow('original', edges)

k = cv.waitKey(0) & 0xFF

if k == '27':
    cv.destroyAllWindows()
