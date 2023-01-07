# 4 clr to gray

import cv2 as cv

img = cv.imread("Resources/puppy.jpg")
cv.imshow("color img",img)

gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray img",gray_img)

cv.waitKey(0)
cv.destroyAllWindows()
