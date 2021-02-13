import cv2 as cv
import numpy as np
#funcion que se ejecuta al cambiar el valor del trackbar
def nothing(x):
    pass

img = np.zeros((100,100,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('value','image', 0, 255,nothing)

while cv.waitKey(60) != ord('p'):
    cv.imshow('image',img)
    
    print(cv.getTrackbarPos('value','image'))

cv.destroyAllWindows()