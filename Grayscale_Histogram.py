import cv2 as cv 
import numpy as np
from matplotlib import pyplot as plt
import sys 

def add_hist(hist, title, pos, color):
    ax = plt.subplot(2, 3, pos)
    plt.title(title)
    plt.xlabel("bins")
    plt.ylabel("number of pixels")
    plt.xlim([0, 256])
    plt.plot(hist, color=color)



if __name__ == '__main__':

    #crear grafica
    plt.figure(figsize =(12,6))
    
    image = cv.imread('./images/grogu.jpg',)

    if image is None:
        sys.exit('No se pudo abrir la imagen')

    #propiedades del histograma
    bins = [256]
    hist_range = [0,256]

    #calcuar histograma
    hist = cv.calcHist(image, [0], None, bins, hist_range)

    add_hist(hist, 'Original', 1, 'k')


    cv.imshow('image',image)
    plt.show()
    cv.waitKey(0)

    cv.destroyAllWindows()