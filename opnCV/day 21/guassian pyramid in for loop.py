import cv2

img = cv2.imread("Resources/baboon.jpg")
cv2.imshow("org",img)
copy = img.copy()
gp = [copy]

for i in range(4):
    copy = cv2.pyrDown(copy)
    gp.append(copy)
    cv2.imshow(("GP"+str(i)),copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
