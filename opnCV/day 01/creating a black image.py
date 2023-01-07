# 2
creattting a black image

import numpy as np
import cv2 as cv

img = np.zeros((500,500),dtype=np.uint8) #black img
img2 = np.ones((500,500),dtype=np.uint8)*255 #white img
cv.imshow("black",img)
cv.imshow("White",img2)
cv.waitKey(0)
cv.destroyAllWindows()
