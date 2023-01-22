import cv2
import numpy as np

def printval(x):
    pass


cv2.namedWindow("org")
img = np.zeros((500,500,3),np.uint8)
# cv2.imshow("org",img) # if namedwindow is not used

cv2.createTrackbar("red","org",0,255,printval)
cv2.createTrackbar("green","org",0,255,printval)
cv2.createTrackbar("blue","org",0,255,printval)
cv2.createTrackbar("ON/OFF","org",0,1,printval)

while True:
    cv2.imshow("org", img)
    r = cv2.getTrackbarPos("red","org")
    g = cv2.getTrackbarPos("green", "org")
    b = cv2.getTrackbarPos("blue", "org")
    s = cv2.getTrackbarPos("ON/OFF","org")
    if s==0:
        img[:]=0
    else:
        img[:]=[b,g,r]
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
