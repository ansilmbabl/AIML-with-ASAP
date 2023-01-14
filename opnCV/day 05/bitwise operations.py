import cv2
import numpy as np

img1 = np.zeros((250,500,3),dtype=np.uint8)
img1[0:200,150:350] = 255
cv2.imshow("image1",img1)

img_1 = np.zeros((250,250,3),dtype=np.uint8)
img_2 = np.ones((250,250,3),dtype=np.uint8) *255

img2 = np.hstack((img_1,img_2))
cv2.imshow("image2",img2)

bitAND = cv2.bitwise_and(img1,img2)
cv2.imshow("bitwise AND",bitAND)

bitOR = cv2.bitwise_or(img1,img2)
cv2.imshow("bitwise OR",bitOR)

bitXOR = cv2.bitwise_xor(img1,img2)
cv2.imshow("bitwise XOR",bitXOR)

bitNOT = cv2.bitwise_not(img1)
cv2.imshow("bitwise NOT",bitNOT)
cv2.waitKey(0)
cv2.destroyAllWindows()
