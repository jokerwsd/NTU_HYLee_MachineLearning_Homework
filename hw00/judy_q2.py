#import a png image and rotate 180 degree
import sys
import numpy as np
import cv2

if len(sys.argv) != 2:
	print("Usage: judy_q2.py [input_image.png]")

image_name = sys.argv[1]

img1=cv2.imread(image_name, 0)
rows,cols = img1.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
img2 = cv2.warpAffine(img1,M,(cols,rows))

cv2.imshow("image",img2)
cv2.waitKey(10000)
cv2.destroyAllWindows()

cv2.imwrite("result/ans2.png", img2)

