
# 2 translating image

import cv2
import numpy as np

img = cv2.imread("Resources/messi5.jpg")
cv2.imshow("org",img)

h,w = img.shape[:2]
print(h,w)

tx = w/4 #translating x value
ty = h/4 #translating y value

t_matrix = np.array([[1,0,tx],[0,1,ty]],dtype=np.float32)

t_img = cv2.warpAffine(img,t_matrix,(w,h))

cv2.imshow("translated",t_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
