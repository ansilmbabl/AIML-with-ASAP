
# flag and userdata 2

import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)

def func(event,x,y,flags,userdata):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),userdata[0],userdata[1],6)
        cv2.imshow("out",img)
        print("event: ",event)
        print("flags : ",flags)
        print("userdata :",userdata)
    if flags == cv2.EVENT_FLAG_LBUTTON + cv2.EVENT_FLAG_CTRLKEY:
        cv2.circle(img,(x,y),30,(0,0,255),6)
        cv2.imshow("out",img)
        print("event: ",event)
        print("flags : ",flags)
        print("userdata :",userdata)

    if event == cv2.EVENT_LBUTTONDOWN and cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),30,(255,0,0),6)
        cv2.imshow("out",img)
        print("event: ",event)
        print("flags : ",flags)
        print("userdata :",userdata)

rad = int(input("color: "))
b = int(input("blue value: "))
g = int(input("green value: "))
r = int(input("red value: "))

clr = (b,g,r)
userdata = [rad,clr]

cv2.imshow("out",img)
cv2.setMouseCallback("out",func,userdata)
cv2.waitKey(0)
cv2.destroyAllWindows()
