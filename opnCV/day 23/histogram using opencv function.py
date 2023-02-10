import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Resources/lena.jpg")

hist = cv2.calcHist([img],[0],mask=None,histSize=[256],ranges=[0,256])
plt.plot(hist)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
