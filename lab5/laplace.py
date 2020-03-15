import cv2 as cv

d_depth = cv.CV_16S
kernel_size = 3
window_name = 'Laplace Demo'
image_name = 'TrinityBikes.jpg'

src = cv.imread(cv.samples.findFile(image_name))

src = cv.GaussianBlur(src, (3, 3), 2.0)
src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
dst = cv.Laplacian(src_gray, d_depth, ksize=kernel_size)
abs_dst = cv.convertScaleAbs(dst)

cv.imshow(window_name, abs_dst)
k = cv.waitKey(0) & 0xFF

if k == '27':
    cv.destroyAllWindows()
