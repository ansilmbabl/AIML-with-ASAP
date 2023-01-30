# 2 Gaussian Blurring
import cv2
img = cv2.imread("Resources/opencv-logo.png")
cv2.imshow("org",img)

gblur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussian blur",gblur)

gblur1 = cv2.GaussianBlur(img,(5,5),10)
cv2.imshow("gaussian blur1",gblur1)

gblur2 = cv2.GaussianBlur(img,(5,5),20)
cv2.imshow("gaussian blur2",gblur2)

cv2.waitKey(0)
cv2.destroyAllWindows()
