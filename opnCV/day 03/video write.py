#video write

import cv2

cap = cv2.VideoCapture("Resources/test.mp4")
fourcc = cv2.VideoWriter_fourcc('M','J','P','G') #or (*'MJPG')
out = cv2.VideoWriter("Resources/1001_1.avi",fourcc,25.0,(640,360))

while cap.isOpened():
    ret,img = cap.read()
    if ret == True:
        cv2.imshow("output",img)
        out.write(img)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
