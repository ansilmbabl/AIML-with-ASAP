import cv2

cap = cv2.VideoCapture("Resources/vtest.avi")
bgs = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

while True:
     ret,frame = cap.read()
     if ret == True:
         fgmask = bgs.apply(frame)
         cv2.imshow("frame",frame)
         cv2.imshow("mask",fgmask)
         if cv2.waitKey(30) == ord("q"):
             break

cap.release()
cv2.destroyAllWindows()
