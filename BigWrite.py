import cv2
import numpy as np

img = np.zeros((600, 800, 3), np.uint8)
cv2.ellipse(img, (360, 166), (200, 130), 0, 0, 360, (225, 225, 225), -1)
cv2.circle(img, (260, 140), 30, (0, 0, 0), -2)
cv2.circle(img, (454, 140), 30, (0, 0, 0), -2)
cv2.line(img, (250, 140), (454, 140), (0, 0, 0), 4)
cv2.ellipse(img, (210, 190), (25, 13), 0, 0, 360, (153, 153, 225), -1)
cv2.ellipse(img, (500, 190), (25, 13), 0, 0, 360, (153, 153, 225), -1)
font =cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'dabai', (290, 340),font, 1.5, (255, 255, 255), 3 )
cv2.imshow("lines", img)
cv2.waitKey()

