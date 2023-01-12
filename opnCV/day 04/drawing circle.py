# 2 drawing circle

import cv2
import numpy as np

img = np.zeros((500,500,3),dtype = np.uint8)
#for i in range()
cv2.circle(img,(250,250),150,(123,125,201),-1)

cv2.imshow("circle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
