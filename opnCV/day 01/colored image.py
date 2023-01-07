# 3
colored img

import numpy as np
import cv2 as cv

red = np.zeros((500,500,3),dtype=np.uint8)
red[::]=[0,0,255] #[b,g,r]

green = np.zeros((500,500,3),dtype=np.uint8)
green[::]=[0,255,0] #[b,g,r]

blue = np.zeros((500,500,3),dtype=np.uint8)
blue[::]=[255,0,0] #[b,g,r]

cv.imshow("red",red)
cv.imshow("green",green)
cv.imshow("blue",blue)

cv.waitKey(0)
cv.destroyAllWindows()
