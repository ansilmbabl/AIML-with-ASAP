import cv2
import numpy as np

img = cv2.imread("Resources/opencv-logo.png")
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grey,(5,5),0)
canny = cv2.Canny(blur,50,100)
# canny = cv2.Canny(canny,50,100)

circles = cv2.HoughCircles(canny,cv2.HOUGH_GRADIENT,1,20,param1=100,param2=50,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
print(circles)

for i in circles[0,:]:
    print(i)
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),3)
    cv2.circle(img, (i[0], i[1]), 3, (255, 0, 0), -1)

cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

img = cv2.imread("Resources/opencv-logo.png")
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(grey,(5,5),0)
#canny = cv2.Canny(blur,50,100)
circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,30,param1=100,param2=50,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
print(circles)

for i in circles[0,:]:
    print(i)
    cv2.circle(img,(i[0],i[1]),i[2],(255,0,0),3)
    cv2.circle(img, (i[0], i[1]), 3, (255, 0, 0), -1)

cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
