# 3 adding text

import cv2
import numpy as np

img = np.zeros((500,500,3),dtype = np.uint8)
cv2.putText(img,"ABCD",(100,250),cv2.FONT_HERSHEY_SIMPLEX,4,(132,46,235),3)

cv2.imshow("text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
