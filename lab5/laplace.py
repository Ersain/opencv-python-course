import cv2

d_depth = cv2.CV_16S
kernel_size = 3
image_name = 'TrinityBikes.jpg'

src = cv2.imread(cv2.samples.findFile(image_name))

src = cv2.GaussianBlur(src, (3, 3), 2.0)
src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
dst = cv2.Laplacian(src_gray, d_depth, ksize=kernel_size)
abs_dst = cv2.convertScaleAbs(dst)

cv2.imshow('Laplace Demo', abs_dst)
k = cv2.waitKey(0) & 0xFF

if k == '27':
    cv2.destroyAllWindows()
