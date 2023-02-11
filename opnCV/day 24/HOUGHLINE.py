# HOUGHLINE

import cv2
import numpy as np
img = cv2.imread("Resources/sudoku.png")
cv2.imshow("org",img)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray_img,50,150)

lines = cv2.HoughLinesP(canny,1,np.pi/180,100,minLineLength=50,maxLineGap=15)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)

cv2.imshow("HoughlineP",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
