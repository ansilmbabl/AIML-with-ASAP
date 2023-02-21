import cv2

cap = cv2.VideoCapture("Resources/vtest.avi")
bgs = cv2.createBackgroundSubtractorKNN(detectShadows=False)

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
cv2.calcHist()
