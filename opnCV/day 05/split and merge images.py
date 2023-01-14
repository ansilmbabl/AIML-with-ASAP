import cv2

img = cv2.imread("Resources/baboon.jpg")

b,g,r = cv2.split(img)

cv2.imshow("BLUE",b)
cv2.imshow("GREEN",g)
cv2.imshow("RED",r)

m_img = cv2.merge((b,g,r))
cv2.imshow("merged image",m_img)

cv2.waitKey(0)
cv2.destroyAllWIndows()
