
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

cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
