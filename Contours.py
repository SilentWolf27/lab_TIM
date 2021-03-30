import cv2 as cv  
import numpy as np 

img = cv.imread('./images/color.png', cv.IMREAD_GRAYSCALE)
img = cv.resize(img, None, fx=0.5, fy=0.5)
w,h = img.shape
img_con = np.zeros((w,h,3), np.uint8)

ret, img = cv.threshold(img, 10, 255, cv.THRESH_BINARY_INV)

contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(img_con, contours, 1, (255,255,255), 2)

m = cv.moments(contours[1])

cx = int(m['m10']/m['m00'])
cy = int(m['m01']/m['m00'])

print(cx, cy)
cv.circle(img_con,(cx,cy), 10,180, -1)

print(cv.contourArea(contours[1]))
print(cv.arcLength(contours[1],True))

x,y,w,h = cv.boundingRect(contours[1])
cv.rectangle(img_con,(x,y), (x+w,y+h),(255),2)

cv.imshow('original', img)
cv.imshow('contornos', img_con)
cv.waitKey(0)