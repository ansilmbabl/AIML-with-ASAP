
# 3 canny

import cv2
img = cv2.imread("Resources/threshold.png",0)
cv2.imshow("org",img)
print(img.dtype)
canny = cv2.Canny(img,0,300)
cv2.imshow("canny",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()
