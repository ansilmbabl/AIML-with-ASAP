##3 otsu'z method

import cv2
img = cv2.imread("Resources/noisy2.png",0)
thr,timg = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
thr1,timg1 = cv2.threshold(img,127,255,cv2.THRESH_OTSU+cv2.THRESH_BINARY)

blr = cv2.GaussianBlur(img,(5,5),0)
thr2,timg2 = cv2.threshold(blr,175,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("orig",img)
cv2.imshow("thr",timg)
cv2.imshow("thr + utsu",timg1)
cv2.imshow("thr + utsu + gblr",timg2)

cv2.waitKey(0)
cv2.destroyAllWindows()
