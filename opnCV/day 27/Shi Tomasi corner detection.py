import cv2
import numpy as np
img = cv2.imread("Resources/chessboard.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
o_img = cv2.goodFeaturesToTrack(gray,100,0.01,10)
o_img = np.int0(o_img)

for i in o_img:
    print(i)
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,(0,0,255),-1)

cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
