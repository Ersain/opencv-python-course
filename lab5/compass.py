import cv2
import numpy as np
np.set_printoptions(threshold=np.nan)
resim = cv2.imread('filter.jpg')
resim = cv2.cvtColor(resim, cv2.COLOR_RGB2GRAY)
h1 = np.array([[5, -3, -3], [-5, 0, -3], [5, -3, -3]], dtype=np.float32)/ 15
h2 = np.array([[-3, -3, 5], [-3, 0, 5], [-3, -3, 5]], dtype=np.float32) / 15
h3 = np.array([[-3, -3, -3], [5, 0, -3], [5, 5, -3]], dtype=np.float32) / 15
h4 = np.array([[-3, 5, 5], [-3, 0, 5], [-3, -3, -3]], dtype=np.float32) / 15
h5 = np.array([[-3, -3, -3], [-3, 0, -3], [5, 5, 5]], dtype=np.float32) / 15
h6 = np.array([[5, 5, 5], [-3, 0, -3], [-3, -3, -3]], dtype=np.float32) / 15
h7 = np.array([[-3, -3, -3], [-3, 0, 5], [-3, 5, 5]], dtype=np.float32) / 15
h8 = np.array([[5, 5, -3], [5, 0, -3], [-3, -3, -3]], dtype=np.float32) / 15
print(h1)
new_img1 = cv2.filter2D(resim, -1, h1)
new_img2 = cv2.filter2D(resim, -1, h2)
new_img3 = cv2.filter2D(resim, -1, h3)
new_img4 = cv2.filter2D(resim, -1, h4)
new_img5 = cv2.filter2D(resim, -1, h5)
new_img6 = cv2.filter2D(resim, -1, h6)
new_img7 = cv2.filter2D(resim, -1, h7)
new_img8 = cv2.filter2D(resim, -1, h8)
cv2.imshow('color_image', new_img1)
cv2.waitKey(0)
cv2.destroyAllWindows()