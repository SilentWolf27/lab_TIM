import cv2 as cv 
import numpy as np 
import sys 

image = cv.imread('./images/sudoku.jpg',cv.IMREAD_GRAYSCALE)
laplacian = cv.Laplacian(image, cv.CV_64F)
sobelx = cv.Sobel(image,cv.CV_64F,1,0,ksize=5)
sobely = cv.Sobel(image,cv.CV_64F,0,1,ksize=5)

sobel = cv.add(sobelx,sobely)

cv.imshow('original', image)
cv.imshow('laplacian',laplacian)
cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('sobel', sobel)
cv.waitKey(0)