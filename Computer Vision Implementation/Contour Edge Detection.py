import numpy as np
import cv2

img = cv2.imread('2.jpg')
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img2, 127, 255, 0)

im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours[0])
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.drawContours(img2, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', img)
#cv2.imshow('Image GRAY', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()