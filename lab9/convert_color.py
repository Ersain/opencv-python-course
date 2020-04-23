import cv2

original = cv2.imread('chess_board.png')
img_rgb = original.copy()

convert_hsv_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

res, mask = cv2.threshold(convert_hsv_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

# Converting color ranges of white and black to yellow and red
img_rgb[mask == 255] = [0, 0, 255]
img_rgb[mask == 0] = [0, 255, 255]

cv2.imshow("Original Image", original)
cv2.imshow("Converted Image", img_rgb)

if cv2.waitKey() == 27:
    cv2.destroyAllWindows()
