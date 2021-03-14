import cv2 as cv 
import numpy as np 
import sys  


image = cv.imread('./images/cat.jpg')

#filtro promediador
kernel_dim = 3
kernel = np.ones((kernel_dim,kernel_dim), np.float32) / (kernel_dim**2)

filter_image = cv.filter2D(image, -1, kernel)

print(filter_image.dtype)
cv.imshow('original', image)
cv.imshow('promediado', filter_image)
cv.waitKey(0)