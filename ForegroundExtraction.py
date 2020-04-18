import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Rishabh.jpg", 1)

img =cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

mask = np.zeros(img.shape[:2], np.uint8)

bgdmodel = np.zeros((1, 65), np.float64)

fgdmodel = np.zeros((1, 65), np.float64)

rect = (150, 0, 200, 300)

cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0), 0, 1).astype('uint8')

img = img*mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
# cv2.rectangle(img, (150, 0), (400, 300), (0, 255, 0), 5)

# plt.imshow(img, cmap="gray", interpolation="bicubic")
# plt.show()
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
