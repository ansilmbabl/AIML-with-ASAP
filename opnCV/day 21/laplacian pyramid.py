import cv2

img = cv2.imread("Resources/road.jpg")
layer = img.copy()

gp = [layer]
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)

for i in range(5,0,-1):
    #lapl = cv2.subtract(gp[i-1],cv2.pyrUp(gp[i])) if error occur due to size mismatch do the following
    level = gp[i - 1]
    explevel = cv2.pyrUp(gp[i])
    lapl = cv2.subtract(level, cv2.resize(explevel, (level.shape[1], level.shape[0])))
    cv2.imshow("Lap"+str(i),lapl)

cv2.waitKey(0)
cv2.destroyAllWindows()
