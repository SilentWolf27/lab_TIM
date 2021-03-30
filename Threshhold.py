import cv2 as cv 

imagen = cv.imread('./images/python-logo.png', cv.IMREAD_GRAYSCALE)
ret, binario = cv.threshold(imagen, 120, 255, cv.THRESH_BINARY)
ret, binario_inv = cv.threshold(imagen, 225, 255, cv.THRESH_BINARY_INV)
ret, trunc = cv.threshold(imagen, 200, 255, cv.THRESH_TRUNC)
ret, zero = cv.threshold(imagen, 120, 255, cv.THRESH_TOZERO)
ret, zero_inv = cv.threshold(imagen, 225, 255, cv.THRESH_TOZERO_INV)

cv.imshow('original', imagen)
cv.imshow('binario', binario)
cv.imshow('binario inv', binario_inv)
cv.imshow('trunc', trunc)
cv.imshow('zero', zero)
cv.imshow('zero inv', zero_inv)

cv.waitKey(0)
cv.destroyAllWindows()