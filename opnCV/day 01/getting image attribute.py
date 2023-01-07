## 5 getting image attribute

import cv2 as cv

img = cv.imread("Resources/puppy.jpg")
cv.imshow("image",img)

print("shape: ",img.shape)
width = img.shape[1] #column
height = img.shape[0] #row
print("width: height = ",(width,height))
print("size: ",img.size)
print("Data type: ",img.dtype)

img2=
cv.waitKey()
cv.destroyAllWindows()
