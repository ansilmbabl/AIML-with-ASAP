
import cv2

img = cv2.imread("Resources/messi5.jpg")
h,w = img.shape[:2]
center = (w//2,h//2)

r_matrix = cv2.getRotationMatrix2D(center,45,.5)
r2_img = cv2.warpAffine(img,r_matrix,(w,h))


cv2.imshow("rotated",r_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
