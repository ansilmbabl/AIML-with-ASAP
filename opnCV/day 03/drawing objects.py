## drawing objects

import cv2
import numpy as np

img = np.zeros((200,200,3),dtype=np.uint8)
img = cv2.line(img,(0,100),(100,150),(0,0,255),10)
cv2.arrowedLine(img,(0,100),(100,100),(0,255,0),10)
cv2.line(img,(0,100),(100,50),(255,0,0),10)


cv2.imshow("output",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
