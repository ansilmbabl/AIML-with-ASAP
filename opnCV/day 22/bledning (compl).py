
import cv2
import numpy as np

apple = cv2.imread("Resources/apple.jpg")
orange = cv2.imread("Resources/orange.jpg")

acopy = apple.copy()
ocopy = orange.copy()

#guassian pyr of apple
a_layer =[]
for i in range(6):
    acopy = cv2.pyrDown(acopy)
    a_layer.append(acopy)
print(len(a_layer))
#guassian pyr of orange
o_layer =[]
for i in range(6):
    ocopy = cv2.pyrDown(ocopy)
    o_layer.append(ocopy)
print(len(o_layer))
#laplacian pyr of apple
lap_apple = [a_layer[-1]]
for i in range(5,0,-1):
    lap = cv2.subtract(a_layer[i-1],cv2.pyrUp(a_layer[i]))
    lap_apple.append(lap)

#laplacian pyr of orange
lap_orange = [o_layer[-1]]
for i in range(5,0,-1):
    lap = cv2.subtract(o_layer[i-1],cv2.pyrUp(o_layer[i]))
    lap_orange.append(lap)

# Apple & Orange half stacking
a_o_pyr = []
for a_p,o_p in zip(lap_apple,lap_orange):
    stack = np.hstack((a_p[:,0:int(a_p.shape[1]//2)],o_p[:,int(o_p.shape[1]//2):]))
    a_o_pyr.append(stack)

# image reconstruction
a_o_reconstruction = a_o_pyr[0]
for i in range(1,6):
    a_o_reconstruction = cv2.pyrUp(a_o_reconstruction)
    a_o_reconstruction = cv2.add(a_o_pyr[i],a_o_reconstruction)

cv2.imshow("blended image",a_o_reconstruction)
cv2.waitKey(0)
cv2.destroyAllWindows()
