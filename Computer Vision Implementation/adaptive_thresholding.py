import cv2
import numpy as np
from matplotlib import pyplot as plt
# Adaptive thresholding gives the better image threshold when different illumination between the picture occurs.
img = cv2.imread("Your Image File.jpg or PNG", 0)
_, th1 = cv2.threshold(img, 146, 251, cv2.THRESH_BINARY) # create a threshold level such that 1st arg is image source, 2nd is threshold value, 3rd is the max value, 4th is threshold type in this case binary as completely black and completely white
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 11) # create a threshold level such that 1st arg is image source, 2nd is threshold maximum value, 3rd is the adaptive threshold method, 4th is threshold type in this case binary and 5th is the block size which decides the neighborhood area and C value.
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 11)

#img, contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imshow("Image", img)
cv2.imshow("th1", th1)
cv2.imshow("th2", th2)
cv2.imshow("th3", th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('A Copy of .PNG or jpg File', th1)
cv2.imwrite('A Copy of .PNG or jpg File', th2)
cv2.imwrite('A Copy of .PNG or jpg File', th3)
cv2.imwrite('A Copy of .PNG or jpg File', img)

#Reference Template:   Name, Date, Title of Program, Code Version, Web Adrress
#Reference: pknowledge, April 28th, 2019, adaptive_thresholding_opencv_python.py, version2, https://gist.github.com/pknowledge/6fd9944c2345b8872b8917257f88a7d1/revisions