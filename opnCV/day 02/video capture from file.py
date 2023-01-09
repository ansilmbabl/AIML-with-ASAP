#2 video capture from file
import cv2
cap=cv2.VideoCapture("Resources/test2.mp4")

while True:
    ret,img = cap.read()
    if ret == True:
        cv2.imshow("output",img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
