#input passing as argument

import argparse
import cv2

parser = argparse.ArgumentParser(description = "Argument data test")
parser.add_argument("--input",help="Path to input image.",default = "D:\AIML\openCV\1\Resources\baboon.jpg")
args = parser.parse_args()
print(args)
print(args.input)
print(type(args))
src = cv2.imread(cv2.sample.findFile(args.input))
if src is None:
	print("could not open or find the image",args.input)
	exit(0)
else:
	cv2.imshow("output",src)

cv2.waitKey(0)
cv2.destroyAllWindows()

## running the programme
## cmd> python argpas.py --input (address)
