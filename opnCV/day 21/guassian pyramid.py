import cv2
img = cv2.imread("Resources/lena.jpg")
print("org shape: ",img.shape)
cv2.imshow("org",img)

gp_img1  = cv2.pyrDown(img)
print("gp1 shape: ",gp_img1.shape)
cv2.imshow("gp1",gp_img1)

gp_img2  = cv2.pyrDown(gp_img1)
print("gp2 shape: ",gp_img2.shape)
cv2.imshow("gp2",gp_img2)

gp_img3  = cv2.pyrUp(gp_img2)
print("gp3 shape: ",gp_img3.shape)
cv2.imshow("gp3",gp_img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
