import cv2 as cv 
import numpy as np
image = cv.imread('./images/grogu.jpg')

#Escalado
image = cv.resize(image,None,fx=0.5, fy=0.5)

rows,cols, chan = image.shape
#rotacion
center = ((cols-1)/2,(rows-1)/2) 
#centro, angulo, escalado
M = cv.getRotationMatrix2D(center,180,1)

image = cv.rotate(image,cv.ROTATE_180) #rotacion desde el centro en multiplos de 90
image = cv.warpAffine(image,M,(cols,rows)) #rotacion desde cualquier punto

#traslacion
tx = -100 #traslacion en X
ty = 20 #traslacion en Y
M = np.float32([[1,0,tx],[0,1,ty]])
image = cv.warpAffine(image,M,(cols,rows))

cv.imshow('imagen', image)
cv.waitKey(0)