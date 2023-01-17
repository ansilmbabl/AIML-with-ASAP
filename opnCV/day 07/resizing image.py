
## 1 resizing image

import cv2
img = cv2.imread("Resources/baboon.jpg")

## downscaling

d_h = 300
d_w = 300
d_dimension = (d_w,d_h)

d_resize = cv2.resize(img,d_dimension,interpolation=cv2.INTER_AREA)

cv2.imshow("org",img)
cv2.imshow("downscale",d_resize)

## upscaling

u_h = 800
u_w = 800
u_dimension = (u_w,u_h)
u_resize = cv2.resize(img,u_dimension,interpolation=cv2.INTER_CUBIC)
u_resize2 = cv2.resize(img,u_dimension,interpolation=cv2.INTER_LINEAR)

cv2.imshow("upscale",u_resize)
cv2.imshow("upscale2",u_resize2)
cv2.waitKey(0)
cv2.destroyAllWindows()
