# finding pixel value for canny edge detection
import numpy as np
import cv2
img = cv2.imread("Resources/threshold.png",0)
cv2.imshow("org",img)
print(img.dtype)
canny = cv2.Canny(img,100,199)
cv2.imshow("canny",canny)

gblur = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussian blur",gblur)

sobelx = cv2.Sobel(gblur,cv2.CV_64F,1,0,ksize=3)
sobelx = np.uint8(np.absolute(sobelx))
cv2.imshow("sobelx",sobelx)

sobely = cv2.Sobel(gblur,cv2.CV_64F,0,1,ksize=3)
sobely = np.uint8(np.absolute(sobely))
cv2.imshow("sobely",sobely)

delta_s = cv2.bitwise_or(sobelx,sobely)
cv2.imshow("sobel out",delta_s)


def cl(event,x,y,flag,par):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(img[y][x])

cv2.setMouseCallback("sobel out",cl)
cv2.waitKey(0)
cv2.destroyAllWindows()
