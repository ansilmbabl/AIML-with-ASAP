import cv2

def clickEvent(event,x,y,flag,userdata):
    if event == cv2.EVENT_RBUTTONDOWN:
        b1 = img[y, x, 0]
        g1 = img[y, x, 1]
        r1 = img[y, x, 2]
        
        textclr = "(" + str(b1) + "," + str(g1) + "," + str(r1) + ")"
        cv2.putText(img,textclr,(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(123,46,231),1)
        cv2.imshow("output",img)

img = cv2.imread("Resources/baboon.jpg")
cv2.imshow("output",img)
cv2.setMouseCallback("output",clickEvent)

cv2.waitKey(0)
cv2.destroyAllWindows()
