import cv2
import numpy as np

img = cv2.imread("Resources/chessboard.png")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

o_img = cv2.cornerHarris(gray,3,3,0.02)
o_img = cv2.dilate(o_img,None)
cv2.imshow("dil",o_img)
img[o_img > 0.01*o_img.max()] = [0,0,255]
print(o_img > 0.01*o_img.max())
cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
