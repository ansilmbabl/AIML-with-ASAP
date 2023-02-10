import cv2
from matplotlib import pyplot as plt

img = cv2.imread("Resources/lena.jpg")

b,g,r = cv2.split(img)

l=[img,b,g,r]
title = ["colored","blue","green","red"]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.hist(l[i].ravel(),256,(0,256))
    plt.title(title[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
