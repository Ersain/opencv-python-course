import cv2

img1 = cv2.imread('gaussian_noise.jpg')
img2 = cv2.imread('salt_n_pepper.jpg')
blur1 = cv2.blur(img1, (20, 20))
blur2 = cv2.blur(img2, (20, 20))

cv2.imshow('blurred gaussian', blur1)
cv2.imshow('blurred salt and pepper', blur2)

key = cv2.waitKey(0) & 0xFF

if key == '27':
    cv2.destroyAllWindows()
