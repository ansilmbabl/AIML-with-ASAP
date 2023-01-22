import cv2
import numpy as np
img = cv2.imread("Resources/smarties.png")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

l_b = np.array([0,100,100])
u_b = np.array([10,255,255])
mask = cv2.inRange(hsv,l_b,u_b)
res = cv2.bitwise_and(img,img,None,mask)

cv2.imshow("org",img)
cv2.imshow("mask",mask)
cv2.imshow("result",res)

cv2.waitKey(0)
cv2.destroyAllWindows()
