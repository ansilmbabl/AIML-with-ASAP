# 1 truncate Tozero inv.tozero thresholding

import cv2
img = cv2.imread("Resources/gradient.png")
print(img.shape)
thr,timg = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
thr,timg1 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
thr,timg2 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
thr,timg3 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
print("threshold value: ",thr)

cv2.imshow("org",img)
cv2.imshow("threshold",timg)
cv2.imshow("threshold trunc",timg1)
cv2.imshow("threshold ToZer",timg2)
cv2.imshow("threshold inv.Tozer",timg3)

cv2.waitKey(0)
cv2.destroyAllWindows()
