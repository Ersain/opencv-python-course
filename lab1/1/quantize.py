import cv2
from PIL import Image

img = cv2.imread('../labka.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_labka.jpg', img_gray)

gray_img = Image.open('grayscale_labka.jpg')

quan2 = gray_img.quantize(2)
quan4 = gray_img.quantize(4)
quan6 = gray_img.quantize(6)

quan2.show('2 colors')
quan4.show('4 colors')
quan6.show('6 colors')

cv2.imshow('original', img)

k = cv2.waitKey(0) & 0xFF

if k == '27':
    cv2.destroyAllWindows()
