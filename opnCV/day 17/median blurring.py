# 3 median blurring
import cv2

img = cv2.imread("Resources/tiger noise.jpg")
cv2.imshow("org",img)

med_blr = cv2.medianBlur(img,4)
cv2.imshow("median blur",med_blr)

cv2.waitKey(0)
cv2.destroyAllWindows()
