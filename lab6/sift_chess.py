import cv2

img = cv2.imread('chess_board.png')
gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.SIFT()
kps = sift.detect(gray_scale, None)

img = cv2.drawKeypoints(gray_scale, kps)

cv2.imshow('SIFT Demo', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
