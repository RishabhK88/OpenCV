import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("watch.jpg", cv2.IMREAD_GRAYSCALE)

#Other options instead of GRAYSCALE(0) are: IMREAD_COLOR(which is BGR):1 and IMREAD_UNCHANGED(which is BGR and alpha channel):-1


#image show using opencv
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#image show using matplotlib
# plt.imshow(img, cmap="gray", interpolation="bicubic")
# plt.plot([50, 100], [80, 100], 'c', linewidth=5) #to draw a line using matplotlib
# plt.show()

#save image
# cv2.imwrite("watchgray.jpg", img) 