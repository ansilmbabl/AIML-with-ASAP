## 4 bilateral filtering
import cv2

img = cv2.imread("Resources/opencv-logo.png")
cv2.imshow("org",img)

biblur = cv2.bilateralFilter(img,5,150,50)
cv2.imshow("bilateral blur",biblur)

cv2.waitKey(0)
cv2.destroyAllWindows()
