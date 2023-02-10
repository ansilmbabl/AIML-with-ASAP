import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Resources/lena.jpg")
color = ("b","g","r")

for i,col in enumerate(color):
    hist = cv2.calcHist([img],[i],mask=None,histSize=[256],ranges= [0,256])
    plt.plot(hist,color = col)

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
