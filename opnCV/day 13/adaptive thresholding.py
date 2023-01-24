# 2 adaptive thresholding

import cv2
img = cv2.imread("Resources/sudoku.png",0)

thr,timg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
mean_thr = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,7,3)
gaus_thr = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,7,3)

cv2.imshow("org",img)
cv2.imshow("threshold",timg)
cv2.imshow("mean",mean_thr)
cv2.imshow("gaus",gaus_thr)

cv2.waitKey(0)
cv2.destroyAllWindows()
