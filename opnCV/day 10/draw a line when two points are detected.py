import cv2
import numpy as np
points=[]

def drawline(event,x,y,glags,userdata):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x,y))
        cv2.circle(img,(x,y),2,(0,0,255),-1)
        if (len(points)>=2):
            cv2.line(img,points[-1],points[-2],(0,255,0),5)
    cv2.imshow("output", img)
    print(points)

img = np.zeros((500,500,3),dtype= np.uint8)

cv2.imshow("output",img)
cv2.setMouseCallback("output",drawline)

cv2.waitKey(0)
cv2.destroyAllWindows()
