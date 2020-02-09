import cv2

img = cv2.imread('../labka.jpg')

yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
hls = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

cv2.imshow('original', img)
cv2.imshow('YUV', yuv)
cv2.imshow('HLS', hls)

k = cv2.waitKey(0) & 0xFF

if k == '27':
    cv2.destroyAllWindows()
