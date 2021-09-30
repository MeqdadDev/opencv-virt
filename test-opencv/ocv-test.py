import cv2

img = cv2.imread('ti.png')

# Displaying the image
cv2.imshow('image', img)

cv2.waitKey(0)