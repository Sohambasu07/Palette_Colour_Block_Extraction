import cv2 as cv
import numpy as np
import imutils as im
import sklearn
import math

def shape_det(c):
    per = cv.arcLength(c, True)
    shp = cv.approxPolyDP(c, 0.03*per, True)
    if len(shp) == 4:
        print(len(shp))
        return len(shp)
    else: return -1

img = cv.imread('D:\Studies\Image Processing Project\\blue_shades.jpg', -1)
resized = im.resize(img, width=600)
sh = resized.shape
H = sh[0]
W = sh[1]
C = sh[2]
gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
cv.imshow("Image", gray)
cv.waitKey(0)
kernel = np.ones((5,5),np.uint8)
blurred = cv.GaussianBlur(gray, (5,5), 0)
#erosion = cv.morphologyEx(gray, cv.MORPH_OPEN, kernel)
ret, thresh = cv.threshold(blurred, 247, 255, cv.THRESH_BINARY_INV)
#thresh =cv.bitwise_xor(thresh, mask)
cnts, hier = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
can = cv.Canny(gray, 0, 50)
cv.imshow("Canny", can)
cv.waitKey(0)
cv.imshow("Thresh", thresh)
cv.waitKey(0)
count = 0
for x in cnts:
    sh_d = shape_det(x)
    if sh_d != 4: continue
    M = cv.moments(x)
    if int(M['m00']) == 0:
        continue
    X = int(M["m10"] / M["m00"])
    Y = int(M["m01"] / M["m00"])
    cv.drawContours(resized, [x], -1, (0, 0, 255), 2)
    co = ''.join((str(X),str(Y)))
    col = str(resized[Y,X])
    col = ''.join(col)
    count += 1
    cv.putText(resized, str(co), (X-3,Y), cv.FONT_HERSHEY_SIMPLEX, 0.3, (255,200,0), 1)
    cv.imshow("Image", resized)
    cv.waitKey(100)
cv.putText(resized, str(count)+" colours present", (W//2-100,H//2), cv.FONT_HERSHEY_DUPLEX, 1, (255,0,100), 2)
cv.imshow("Image", resized)
cv.waitKey(0)
