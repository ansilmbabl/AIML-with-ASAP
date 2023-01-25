
# 4 subplot

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Resources/gradient.png")
thr0,timg0 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
thr,timg = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
thr1,timg1 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
thr2,timg2 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
thr3,timg3 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ["org","BINARY","BINARY_INV","TRUNC","TOZERO","TOZERO_INV"]
images = [img,timg0,timg,timg1,timg2,timg3]

for i in range(len(images)):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
