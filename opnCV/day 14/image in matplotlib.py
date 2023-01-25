
# 3 image in matplotlib
import matplotlib.pyplot as plt
import cv2

img = cv2.imread("Resources/messi5.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.xticks([])
plt.yticks([])

plt.imshow(img)
plt.show()
