
## 2 perspective transformation

import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")
w,h = 250,350

# card 1
pts1 = np.float32([[170,80],[255,80],[257,203],[171,203]])
pts2 = np.float32([[0,0],[w,0],[w,h],[0,h]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgout = cv2.warpPerspective(img,matrix,(w,h))
cv2.imshow("org",img)
cv2.imshow("perspective",imgout)

# card 2
pts3 = np.float32([[116,181],[195,216],[64,290],[133,329]])
pts4 = np.float32([[0,0],[w,0],[0,h],[w,h]])
matrix2 = cv2.getPerspectiveTransform(pts3,pts4)
imgout2 = cv2.warpPerspective(img,matrix,(w,h))
cv2.imshow("persp 2",imgout2)

cv2.waitKey(0)
cv2.destroyAllWindows()
