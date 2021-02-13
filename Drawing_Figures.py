import cv2 as cv 
import numpy as np
 
#crear una imagen
img = np.zeros((250,500,3), np.uint8)

#dibujar una linea
#imagen, punto1, punto2, color, grosor
cv.line(img, (0,0), (500,250), (255,0,0), 3)

#dibujar rectangulo
#imagen, punto1, punto2, color, grosor
cv.rectangle(img, (100,100), (200,200),(0,255,0), 2)

#dibujar circulo
#imagen, centro, radio, color, grosor
cv.circle(img, (400,100), 25, (0,0,255), 2)

cv.imshow('imagen',img)
cv.waitKey(0)

cv.destroyAllWindows()