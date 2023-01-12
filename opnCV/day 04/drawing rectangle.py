# 1 drawing rectangle

import cv2
import numpy as np

img = np.zeros((500,500,3),dtype = np.uint8)
cv2.rectangle(img,(100,100),(250,250),(120,240,100),5)
#cv2.rectangle(img,(100,100),(250,250),(120,240,100),-1) #--> filled rectangle
#cv2.rectangle(img,(100,100),(250,250),(120,240,100),cv2.FILLED) #--> filled rectangle

cv2.imshow("rectangle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
