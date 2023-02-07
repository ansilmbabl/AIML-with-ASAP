import cv2

imgo = cv2.imread("Resources/contour_understanding.jpg")
cv2.imshow("originalk",imgo)
img = cv2.cvtColor(imgo,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",img)
thr,b_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cnt,hr = cv2.findContours(b_img,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgo,cnt,-1,(0,255,0),3)
cv2.imshow("out",imgo)
cv2.waitKey(0)
cv2.destroyAllWindows()
