## 1 grayscale video

import cv2
vid = cv2.VideoCapture("Resources/test.mp4")

while True:
    ret,img = vid.read()
    if ret == True:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converting color image to grayscale
        cv2.imshow("output",img)
    if cv2.waitKey(1) == ord("q"):
        break

vid.release()
cv2.destroyAllWindows()
