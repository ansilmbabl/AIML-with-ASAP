import cv2
import numpy as np

img  = cv2.imread("Resources/WNflZ.png",0)
kernel = np.ones((3,3),np.uint8)

open = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
close = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
morph_grad = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("org",img)
cv2.imshow("open",open)
cv2.imshow("close",close)
cv2.imshow("morph_grad",morph_grad)
cv2.imshow("tophat",tophat)
cv2.imshow("blackhat",blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()
