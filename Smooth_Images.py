import cv2 as cv 
import numpy as np 
import sys  


image = cv.imread('./images/sal_pimienta.jpg')

blur = cv.GaussianBlur(image, (5,5),0)
median = cv.medianBlur(image,5)


cv.imshow('original', image)
cv.imshow('blur', blur)
cv.imshow('median', median)
cv.waitKey(0)