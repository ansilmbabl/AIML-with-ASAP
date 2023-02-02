
## changing threshold value of canny by trackbar

import cv2
img = cv2.imread("Resources/baboon.jpg",0)
cv2.imshow("org",img)
print(img.dtype)

def cl(x):
    pass

cv2.namedWindow("track")
cv2.createTrackbar("thr1","track",0,255,cl)
cv2.createTrackbar("thr2","track",0,255,cl)

while True:
    t1 = cv2.getTrackbarPos("thr1", "track")
    t2 = cv2.getTrackbarPos("thr2", "track")
    canny = cv2.Canny(img,t1,t2)
    cv2.imshow("canny",canny)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
