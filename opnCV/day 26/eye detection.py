## eye detection

import cv2

face_c = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
eye_c = cv2.CascadeClassifier("Resources/haarcascade_eye_tree_eyeglasses.xml")
img = cv2.imread("Resources/lena.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
faces = face_c.detectMultiScale(img,1.1)
print("faces :",faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    fac_gray = gray[y:y+h,x:x+w]
    fac_color = img[y:y+h,x:x+w]
    eyes = eye_c.detectMultiScale(fac_gray)
    print("eyes: ",(eyes))

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(fac_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
