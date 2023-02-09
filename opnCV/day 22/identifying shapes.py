# identifying shape

import cv2

img = cv2.imread("Resources/shapes.jpg")

greyimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(greyimg,(5,5),1)
canny = cv2.Canny(imgblur,50,100)

cnt,hr = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
print(cnt)

for ct in cnt:
    area = cv2.contourArea(ct)
    if area > 500:
        approx =  cv2.approxPolyDP(ct,0.01*cv2.arcLength(ct,True),True)
        cv2.drawContours(img,[approx],0,(0,255,0),2)
        obj = len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        print(x,y,w,h)
        if obj == 3:
            object_name = "Triangle"
        elif obj == 4:
            if w==h:
                object_name = "Square"
            else:
                object_name = "Rectangle"
        elif obj == 5:
            object_name = "Pentagon"
        elif obj > 15:
            object_name = "Circle"
        else:
            object_name = "Ellipse"

        # cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) bounding rectangle
        cv2.putText(img,object_name,(x+(w//2),y+(h//2)),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)

cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
