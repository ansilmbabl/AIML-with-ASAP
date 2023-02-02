# 2 laplacian

import cv2
import numpy as np
import matplotlib as plt

img = cv2.imread("Resources/blackandwhite.jpg")
cv2.imshow("org",img)

lap = cv2.Laplacian(img,cv2.CV_64F,ksize=5,scale = 2)
lap = np.uint8(np.absolute(lap))
cv2.imshow("lap",lap)

lap1 = cv2.Laplacian(img,cv2.CV_64F,ksize=5,scale = 1)
lap1 = np.uint8(np.absolute(lap1))
cv2.imshow("lap1",lap1)

cv2.waitKey(0)
cv2.destroyAllWindows()
