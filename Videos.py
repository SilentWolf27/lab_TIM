import cv2 as cv 
import numpy as np 
import sys

#crear una captura de video
cap = cv.VideoCapture(0)

if not cap.isOpened():
    sys.exit('No se pudo abrir la camara')

while cv.waitKey(60) != ord('p'):
    #capturar un frame
    ret, frame = cap.read()

    if not ret:
        print('No se recivio ningun frame... El programa se cerrara.')
        break

    cv.imshow('video', frame)

#Liberar memoria de la captura
cap.release()
cv.destroyAllWindows()