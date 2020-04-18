import cv2
import numpy as np

img = cv2.imread("bookpage.jpg", 1)

retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval2, threshold2 = cv2.threshold(gray_scale, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(gray_scale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 155, 1)

retval3, otsu = cv2.threshold(gray_scale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("img", img)
cv2.imshow("threshold", threshold)
cv2.imshow("threshold2", threshold2)
cv2.imshow("gaus", gaus)
cv2.imshow("otsu", otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
