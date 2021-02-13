import cv2 as cv
import sys

img = cv.imread('./images/grogu.jpg',cv.IMREAD_COLOR)

roi = img[250:500, 250:500]

cv.imshow('roi',roi)
cv.waitKey(0)
cv.destroyAllWindows()
