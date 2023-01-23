# 1 detecting color with the trackbar

import cv2
import numpy as np

def printVal(x):
    pass

cv2.namedWindow("HSV_Color_Space")

cv2.createTrackbar("LowerH","HSV_Color_Space",0,179,printVal)
cv2.createTrackbar("LowerS","HSV_Color_Space",0,255,printVal)
cv2.createTrackbar("LowerV","HSV_Color_Space",0,255,printVal)
cv2.createTrackbar("UpperH","HSV_Color_Space",179,179,printVal)
cv2.createTrackbar("UpperS","HSV_Color_Space",255,255,printVal)
cv2.createTrackbar("UpperV","HSV_Color_Space",255,255,printVal)

while True:
    img = cv2.imread("Resources/smarties.png")
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("LowerH","HSV_Color_Space")
    l_s = cv2.getTrackbarPos("LowerS","HSV_Color_Space")
    l_v = cv2.getTrackbarPos("LowerV","HSV_Color_Space")
    u_h = cv2.getTrackbarPos("UpperH","HSV_Color_Space")
    u_s = cv2.getTrackbarPos("UpperS","HSV_Color_Space")
    u_v = cv2.getTrackbarPos("UpperV","HSV_Color_Space")

    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s, u_v])

    mask = cv2.inRange(hsv,l_b,u_b)
    res = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow("original",img)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)

    if cv2.waitKey(1) == ord("q"):
        break
cv2.destroyAllWindows()
