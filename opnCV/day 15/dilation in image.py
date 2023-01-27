import cv2
import numpy as np

kernel = np.ones((3,3),np.uint8)

img =  cv2.imread("Resources/jchar.png")
thr,t_img  = cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
dil = cv2.dilate(img,kernel,iterations=1)

cv2.imshow("org",img)
cv2.imshow("thresh",t_img)
cv2.imshow("dilated",dil)
cv2.waitKey(0)
cv2.destroyAllWindows()
