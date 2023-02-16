# object detection (face)

import cv2

face_c = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/lena.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
faces = face_c.detectMultiScale(img,1.1)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
