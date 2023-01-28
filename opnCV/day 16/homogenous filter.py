import cv2
import numpy as np

img =cv2.imread("Resources/opencv-logo.png")
cv2.imshow("org",img)
print(img.dtype)

kernel = np.ones((5,5),np.float64)/25
print(kernel.dtype)
dst = cv2.filter2D(img,-1,kernel)
print(dst.dtype)

kernel2 = np.ones((7,7),np.float32)/25
print(kernel2.dtype)
dst2 = cv2.filter2D(img,-1,kernel2)
print(dst2.dtype)

cv2.imshow("out",dst)
cv2.imshow("out2",dst2)
cv2.waitKey(0)
cv2.destroyAllWindows()
