import cv2 as cv
img = cv.imread("Resources/puppy.jpg")
cv.imshow("image",img)
cv.imwrite("Resources/puppy2.jpg",img)
s_img= cv.imread("Resources/puppy.jpg")
cv.imshow("saved image",s_img)
cv.waitKey(0)
cv.destroyAllWindows()
