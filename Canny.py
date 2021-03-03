import cv2 as cv 
import numpy as np 
import sys

image = cv.imread('./images/mano.jpg',cv.IMREAD_GRAYSCALE)


canny = cv.Canny(image, 70, 50)

cv.imshow('original', image)
cv.imshow('canny', canny)


cv.waitKey(0)