import cv2
import numpy as np

img = cv2.imread('chess_board.png')
gray_scale = np.float32(
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
)

detector_responses = cv2.cornerHarris(gray_scale, 2, 3, 0.04)
detector_responses = cv2.dilate(detector_responses, None)

img[detector_responses > 0.01 * detector_responses.max()] = [0, 0, 255]
cv2.imshow('Harris Demo', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
