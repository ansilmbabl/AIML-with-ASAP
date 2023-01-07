#importing cv module
# import cv2
# print("import success")

import cv2

gray_img = cv2.imread("Resources/puppy.jpg",0)
clr_img = cv2.imread("Resources/puppy.jpg",1)
unch_img = cv2.imread("Resources/puppy.jpg",-1) #or cv2.IMREAD_UNCHANGED

cv2.imshow("Gray Image",gray_img)
cv2.imshow("Color Image",clr_img)
cv2.imshow("Unchanged Image",unch_img)

print("read successfully")
cv2.waitKey(3000) #wait for 3 seconds
cv2.destroyAllWindows() #destroys all windows from the memory by pressing any key
