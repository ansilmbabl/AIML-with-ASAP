#3 video capture from cam
import cv2
cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret,img = cap.read()
    if ret == True:
        cv2.imshow("output",img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
