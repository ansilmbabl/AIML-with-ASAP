
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Resources/baboon.jpg")
copy = img.copy()
gp = [copy]
titles = ["GP original"]

n = int(input("number of layers: "))
for i in range(n):
    copy = cv2.pyrDown(copy)
    gp.append(copy)
    name = "GP"+str(i+1)
    titles.append(name)

print(titles)
#displaying in matplotlib
for i in range(n+1):
    plt.subplot((n+1)//2,(n+1)//2,i+1)
    plt.imshow(gp[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
