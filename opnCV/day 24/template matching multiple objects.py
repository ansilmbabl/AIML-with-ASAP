import cv2
import numpy as np

img = cv2.imread("Resources/mario.jpg")
t_img = cv2.imread("Resources/mario_coin.png")

w,h = t_img.shape[1],t_img.shape[0]
t_img = cv2.matchTemplate(img,t_img,cv2.TM_CCORR)
print(t_img)
print(t_img.dtype)

thresh = 0.8

loc = np.where(t_img>thresh)
for pt in zip(loc[0],loc[1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h),255,2)
cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
