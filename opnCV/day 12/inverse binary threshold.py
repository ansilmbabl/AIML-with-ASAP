
# 3 inverse binary threshold

import cv2
img = cv2.imread("Resources/gradient.png")

thr,timg = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
print("threshold value: ",thr)

cv2.imshow("org",img)
cv2.imshow("threshold",timg)
cv2.waitKey(0)
cv2.destroyAllWindows()
