import cv2
import numpy as np

img = cv2.imread("watch.jpg", 1)


#To print the actual color value of pixel
#px = img[address of pixel]
px = img[55, 55]
#print(px)

#change color of pixel
img[55, 55] = [0, 0, 0]
px = img[55, 55]
print(px)


#ROI-Region Of Image-It is like sub image of an image
#change color of subimage(roi)
roi = img[200:300, 200:300] = [0, 0, 0]
print(roi)


#to copy and paste one region of image to another region of image
timex = img[500:600, 800:900]
img[0:100, 0:100] = timex


cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

