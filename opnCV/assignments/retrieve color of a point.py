## HW
"""
Trial Program:
Read an image and when we click on any point,
it should retrieve the color of that point and show it in different window.
"""

import cv2
import numpy as np

def clrpicker(events,x,y,flags,params):
    cv2.imshow("color", clr)
    if events == cv2.EVENT_LBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x, 1]
        r = img[y,x, 2]
        print(b,g,r)

        clr[:] = [b,g,r]
        cv2.imshow("color",clr)


img = cv2.imread("Resources/baboon.jpg")
clr = np.ones((200, 200, 3), np.uint8) * 255

cv2.imshow("out",img)
cv2.setMouseCallback("out",clrpicker)

cv2.waitKey(0)
cv2.destroyAllWindows()
