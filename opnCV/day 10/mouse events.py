import cv2
import numpy as np

def clickEvent(event,x,y,flags,userdata):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = "(" + str(x) + "," + str(y) + ")"
        cv2.putText(img,text,(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),1)
        cv2.imshow("output",img)
        print("Event : ",event)
        print("flags : ",flags)
        print("userdata : ",userdata)

img = np.zeros((500,500,3),dtype=np.uint8)
cv2.imshow("output",img)
cv2.setMouseCallback("output",clickEvent)
cv2.waitKey(0)
cv2.destroyAllWindows()
