# 1 sobel

import cv2
import numpy as np

img =cv2.imread("Resources/blackandwhite.jpg")
cv2.imshow("org",img)

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0)
sobelx = np.uint8(np.absolute(sobelx))
cv2.imshow("sobelx",sobelx)

sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobely = np.uint8(np.absolute(sobely))
cv2.imshow("sobely",sobely)

delta_s = cv2.bitwise_or(sobelx,sobely)
cv2.imshow("sobel out",delta_s)

cv2.waitKey(0)
cv2.destroyAllWindows()
