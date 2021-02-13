import cv2 as cv
import sys

img = cv.imread('./images/grogu.jpg',cv.IMREAD_COLOR)

#obtener cada canal por separado
b,g,r = cv.split(img)

#mezclar canales
img = cv.merge((r,g,b))

cv.imshow('Opuesto',img)
cv.waitKey(0)
cv.destroyAllWindows()