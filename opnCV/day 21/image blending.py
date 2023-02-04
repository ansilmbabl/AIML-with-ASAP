import cv2
import numpy as np

apple = cv2.imread("Resources/apple.jpg")
orange = cv2.imread("Resources/orange.jpg")

img = np.hstack((apple[:,0:apple.shape[1]//2],orange[:,orange.shape[1]//2:]))
cv2.imshow("Stacked img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()
