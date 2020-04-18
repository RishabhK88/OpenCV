import cv2
import numpy as np

img1 = cv2.imread("3D-Matplotlib.png", 1)
img2 = cv2.imread("mainsvmimage.png", 1)
img3 = cv2.imread("mainlogo.png", 1)

# add = img1 + img2     in this method picture pretty much retains its opacity

#or

#in this method the picture is very whitish the reason it that it adds the pixel values together so say 
#(155, 211, 79) + (50, 170, 200) = 205, 381, 279 this max is 255, it translates to (205, 255, 255) 
#which is why image is extremely whitish 
# add = cv2.add(img1, img2)

#or

#more ideal method..gives weight to each image, so img1 say should be 60% of final and img2, the rest 40% as shown below
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

ret, mask  = cv2.threshold(img3gray, 220, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)

img1[0:rows, 0:cols] = dst

cv2.imshow("res", img1)
cv2.imshow("mask_inv", mask_inv)
cv2.imshow("img1_bg", img1_bg)
cv2.imshow("img3_fg", img3_fg)
cv2.imshow("dst", dst)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()