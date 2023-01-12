# 4 text i video (webcam)

import cv2
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while cap.isOpened():
    ret,img = cap.read()
    w,h = cap.get(3),cap.get(4)
    text = f"({w},{h})"

    if ret == True:
        cv2.putText(img,text,(100,100),6,2,(121,45,132),4)
        cv2.imshow("output",img)
    if cv2.waitKey(-1) == ord("q"):
        break
cap.release()
