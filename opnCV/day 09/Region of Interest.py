
import cv2

img = cv2.imread("Resources/messi5.jpg")
r = cv2.selectROI(img,showCrosshair=False,fromCenter=False)
img_crop = img[r[1]:r[1]+r[3],r[0]:r[0]+r[2]]
cv2.imshow("cropped",img_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
