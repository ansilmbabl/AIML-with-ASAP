
# 5 morphological operations

import cv2
import numpy as np

img = cv2.imread("Resources/sudoku.png",0)
print(img.shape)

kernel = np.ones((3,3),np.uint8)
ero_img = cv2.erode(img,kernel,iterations=1)
dil_img = cv2.dilate(img,kernel,iterations=1)
cv2.imshow("org",img)
cv2.imshow("eroded",ero_img)
cv2.imshow("dilated",dil_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
