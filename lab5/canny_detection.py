import cv2

img = cv2.imread('TrinityBikes.jpg', 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('original', edges)

k = cv2.waitKey(0) & 0xFF

if k == '27':
    cv2.destroyAllWindows()
