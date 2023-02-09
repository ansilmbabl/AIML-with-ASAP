
import cv2

cap = cv2.VideoCapture("Resources/vtest.avi")
ret,frame1 = cap.read()
ret,frame2 = cap.read()

while cap.isOpened():
    difference = cv2.absdiff(frame1,frame2)
    grey = cv2.cvtColor(difference,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(5,5),0)
    canny = cv2.Canny(blur,50,100)
    cv2.imshow("canny", canny)
    dilation = cv2.dilate(canny,(5,5))
    contour, hirearchy = cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    for cnt in contour:
        x,y,w,h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area < 500:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("img",frame1)
    frame1 = frame2
    ret, frame2 = cap.read()
    if cv2.waitKey(25) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
