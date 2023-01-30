# 1 averaging

import cv2

img = cv2.imread("Resources/opencv-logo.png")
cv2.imshow("org",img)

blur = cv2.blur(img,(5,5))
cv2.imshow("blurred image",blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
