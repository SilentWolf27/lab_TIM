#Importar OpenCV
import cv2 as cv
import numpy as np
import sys
 
#Leer Imagen
img = cv.imread('./images/grogu.jpg',cv.IMREAD_COLOR)

if img is None: 
    sys.exit('No se pudo leer la imagen')

#Propiedades de una imagen
h,w,c = img.shape

#modificando un pixel
img[10,10] =  [255,255,255]
#mejor forma
blue = img.item(11,11,0)
img.itemset((11,11,0),blue + 100)



#Mostrar Imagen
cv.namedWindow('Grogu',cv.WINDOW_AUTOSIZE)
cv.imshow('Grogu',img)
#Capturar Tecla
cv.waitKey(0)

cv.destroyAllWindows()
#Guardar Imagen
cv.imwrite('./imagen.jpg',img)