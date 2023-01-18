
# 1 cropping

import cv2

img = cv2.imread("Resources/messi5.jpg")
cv2.imshow("org",img)

crop_img = img[294:348,336:387] #[63,51]
cv2.imshow("cropped img",crop_img)

img[294:342,0:51] = crop_img
cv2.imshow("modif",img)

img[0:48,0:51] = crop_img
cv2.imshow("modified",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
