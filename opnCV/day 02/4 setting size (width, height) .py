##4 setting size (width, height) --> get/set
import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,img = cap.read()
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
    w,h=cap.get(3),cap.get(4)
    print(w,h)
    if ret == True:
        cv2.imshow("output",img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindow.0.0s()
