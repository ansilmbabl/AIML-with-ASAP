# 2 resizing with aspect ratio

import cv2

img = cv2.imread("Resources/puppy.jpg")
r_img = cv2.resize(img,(300,300))

w = 500
aspect_ratio = 500/img.shape[1]
print(aspect_ratio)

r_img_aspr = cv2.resize(img,(int(img.shape[1]*aspect_ratio),int(img.shape[0]*aspect_ratio)))

cv2.imshow("image",img)
cv2.imshow("resize",r_img)
cv2.imshow("resize with aspect ratio",r_img_aspr)

cv2.waitKey(0)
cv2.destroyAllWindows()
