
import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny_method(img):
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,100)
    return canny

def region_of_interest(img):
    height = img.shape[0]
    tri_part = np.array([[(200,height),(1100,height),(550,250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask,tri_part,255)
    m_img = cv2.bitwise_and(image,mask)
    return m_img

def disp_lines(img,lines):
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,255,255),3)
    return img


image = cv2.imread("Resources/test_image.png")
o_img = np.copy(image)
canny = canny_method(o_img)
roi_image = region_of_interest(canny)
cv2.imshow("roi",roi_image)

#lines = cv2.HoughLinesP(roi_image,2,np.pi/180,200,minLineLength=20,maxLineGap=20)
lines = cv2.HoughLinesP(roi_image,2,np.pi/180,200,minLineLength=20,maxLineGap=20)
print(lines)
l_img = disp_lines(image,lines)
cv2.imshow("out",l_img)

plt.imshow(canny)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
