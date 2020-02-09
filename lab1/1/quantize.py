import cv2
from PIL import Image
import PIL

img = cv2.imread('../labka.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('grayscale_labka.jpg', img_gray)

im1 = Image.open('grayscale_labka.jpg')

im1 = im1.quantize(6)

im1.show()
