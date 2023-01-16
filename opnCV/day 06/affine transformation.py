
## 1 affine transformation

import cv2
import numpy as np

img = cv2.imread("Resources/puppy.jpg")
w,h = img.shape[1],img.shape[0]
print(w,h)

pts1 = np.float32([[0,0],[304,0],[304,234]])  #source
pts2 = np.float32([[25,100],[304,0],[304,234]]) #destination

matrix = cv2.getAffineTransform(pts1,pts2)
imgout = cv2.warpAffine(img,matrix,(w,h))

cv2.imshow("org",img)
cv2.imshow("affined",imgout)

cv2.waitKey(0)
cv2.destroyAllWindows()
