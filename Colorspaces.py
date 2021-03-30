import cv2 as cv 

img = cv.imread('./images/lenna.png',cv.IMREAD_COLOR)

img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

cv.imshow('image',img)
cv.waitKey(0)