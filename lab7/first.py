import cv2

original_img = cv2.imread('supremacy.jpg', 0)
template = cv2.imread('template_from_original.png', 0)
w, h = template.shape[::-1]

method = cv2.TM_CCOEFF

result = cv2.matchTemplate(
    original_img, template, method
)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

cv2.imshow('Original', original_img)

cv2.rectangle(original_img, top_left, bottom_right, 255, 2)
cv2.imshow('Supremacy Detection', original_img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
