import cv2

img1 = cv2.imread("Resources/puppy.jpg")
img2 = cv2.imread("Resources/puppy.png")

img1 = cv2.resize(img1,(500,500)) #resizing image
img2 = cv2.resize(img2,(500,500))

#add_img = cv2.add(img1,img2) #adding images
add_img = cv2.addWeighted(img1,.2,img2,.8,0) #images with opacity cotrole

cv2.imshow("added image",add_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
