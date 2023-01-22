## HW
"""
read an image and create a switch trackbar, if 1 is set, display the image as it is,
if 0 is set, grayscale image should be displayed
"""

import cv2
import numpy as np

def val(x):
    pass

img = cv2.imread("Resources/puppy.jpg")
cv2.imshow("out", img)
cv2.createTrackbar("show image","out",0,1,val)

while True:
    cv2.imshow("out", img)
    switch = cv2.getTrackbarPos("show image","out")
    if switch == 1:
        cv2.imshow("out", np.zeros((img.shape[0],img.shape[1]),np.uint8))
    if cv2.waitKey(1)==ord("q"):
        break
cv2.destroyAllWindows()
