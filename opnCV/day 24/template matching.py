import cv2

img = cv2.imread("Resources/messi5.jpg",0)
t_img = cv2.imread("Resources/messi_face.jpg",0)

w,h = t_img.shape[1],t_img.shape[0]
t_img = cv2.matchTemplate(img,t_img,cv2.TM_CCOEFF)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(t_img)

top_l = max_loc
bot_r = top_l[0]+w,top_l[1]+h

cv2.rectangle(img,top_l,bot_r,255,2)
cv2.imshow("out",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
