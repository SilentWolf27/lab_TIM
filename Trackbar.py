import cv2 as cv
import numpy as np
#funcion que se ejecuta al cambiar el valor del trackbar
def nothing(x):
    pass

img = np.zeros((100,100,3), np.uint8)
cv.namedWindow('image')

# create trackbars for color change
cv.createTrackbar('red','image', 0, 255,nothing)
cv.createTrackbar('green','image', 0, 255,nothing)
cv.createTrackbar('blue','image', 0, 255,nothing)

while cv.waitKey(60) != ord('p'):
    red = cv.getTrackbarPos('red','image')
    green = cv.getTrackbarPos('green','image')
    blue = cv.getTrackbarPos('blue','image')
    
    img[:,:,0] = blue
    img[:,:,1] = green
    img[:,:,2] = red

    cv.imshow('image',img)

cv.destroyAllWindows()