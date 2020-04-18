import cv2
import numpy as np

img = cv2.imread("watch.jpg", 1)

cv2.line(img, (0, 0), (300, 300), (255, 0, 0), 15)

cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)

cv2.circle(img, (100, 163), 55, (0, 0, 255), -1)
# linewidth=-1 like above fills the shape

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)

#pts = pts.reshape((-1, 1, 2))

cv2.polylines(img, [pts], True, (0, 0, 0), 5)
# true is whether or not to connect last point to first one

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV Tuts!!!", (0, 130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("image", img)

cv2.waitKey(0)

cv2.destroyAllWindows()