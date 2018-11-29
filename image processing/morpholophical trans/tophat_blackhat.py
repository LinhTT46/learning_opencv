import cv2
import numpy as np 

img = cv2.imread('j.png', 0)

kernel = np.ones((9, 9), np.uint8)

# tophat = src - open()
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# blackhat = close() - src
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('original', img)
cv2.imshow('tophat', tophat)
cv2.imshow('blackhat', blackhat)
cv2.waitKey(0)
cv2.destroyAllWindows()