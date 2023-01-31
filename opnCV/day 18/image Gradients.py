
# import cv2
#
# img = cv2.imread("Resources/messi5.jpg")
# cv2.imshow("org",img)
#
# scharx = cv2.Scharr(img,-1,1,0)
# cv2.imshow("scx",scharx)
# schary = cv2.Scharr(img,-1,0,1)
# cv2.imshow("scy",schary)
# delta_s = cv2.bitwise_and(scharx,schary)
# cv2.imshow("scharr",delta_s)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread("Resources/blackandwhite.jpg")
cv2.imshow("org",img)

scharx = cv2.Scharr(img,cv2.CV_64F,1,0)
scharx = np.uint8(np.absolute(scharx))
cv2.imshow("scx",scharx)

schary = cv2.Scharr(img,cv2.CV_64F,0,1)
schary = np.uint8(np.absolute(schary))
cv2.imshow("scy",schary)

delta_s = cv2.bitwise_and(scharx,schary)
cv2.imshow("scharr",delta_s)
      
cv2.waitKey(0)
cv2.destroyAllWindows()
