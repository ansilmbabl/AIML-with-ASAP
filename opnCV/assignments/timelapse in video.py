#2 timelapse in video

import cv2
import time
#import datetime

vid = cv2.VideoCapture("Resources/test.mp4")
start = time.time()
while True:
    ret,img = vid.read()

    if ret == True:
        end = time.time()
        #cv2.putText(img, str(datetime.datetime.now()), (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (123, 123, 123), 2)
        cv2.putText(img, f"{end - start :.2f}", (0, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (123, 123, 123), 2)
        cv2.imshow("output",img)

    if cv2.waitKey(1) == ord("e"):
        break

vid.release()
cv2.destroyAllWindows()
