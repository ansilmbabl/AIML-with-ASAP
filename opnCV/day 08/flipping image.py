
# 3 flipping image

import cv2

img = cv2.imread("Resources/messi5.jpg")

f_x_img = cv2.flip(img,0)
f_y_img = cv2.flip(img,1)
f_xy_img = cv2.flip(img,-1)

cv2.imshow("org",img)
cv2.imshow("flip X",f_x_img)
cv2.imshow("flip Y",f_y_img)
cv2.imshow("flip XY",f_xy_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
