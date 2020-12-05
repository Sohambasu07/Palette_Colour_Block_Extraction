import cv2 as cv
import numpy as np
import math


def shape_det(c):
    per = cv.arcLength(c, True)
    shp = cv.approxPolyDP(c, 0.01*per, True)
    return shp


img = cv.imread('D:\Studies\Image Processing Project\pink_shades.jpg', -1)
sh = img.shape
H = sh[0]
W = sh[1]
C = sh[2]
w = math.floor(W)
h = math.floor(H)
img = cv.resize(img, (w, h))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blurred = cv.GaussianBlur(gray, (5, 5), 0)
cv.namedWindow("Image", cv.WINDOW_NORMAL)
cv.imshow("Image", img)
cv.resizeWindow("Image", 700, 700)
cv.waitKey(0)
ret, thresh = cv.threshold(blurred, 240, 255, cv.THRESH_BINARY_INV)
#thresh = cv.adaptiveThreshold(blurred, 240, cv.ADAPTIVE_THRESH_MEAN_C, cv.TH   RESH_BINARY_INV, 11, 2)
cnts, hier = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.namedWindow("Thresh", cv.WINDOW_NORMAL)
cv.imshow("Thresh", thresh)
cv.resizeWindow("Thresh", 700, 700)
cv.waitKey(0)
count = 0
palette = []
cnts = np.flip(cnts)
for x in cnts:
    k = len(shape_det(x))
    if k != 4:
        continue
    print(k)
    M = cv.moments(x)
    # print(M,count)
    if int(M['m00']) == 0:
        # X = Y = 0
        continue
    else:
        X = int(M["m10"] / M["m00"])
        Y = int(M["m01"] / M["m00"])
    co = ''.join((str(X), str(Y)))
    col = list(map(int, img[Y, X]))
    if col == (255, 255, 255) and col  or col == (0,0,0):
        continue
    cv.drawContours(img, [x], -1, ((255 - col[0]), (255 - col[1]), (255 - col[2])), 2)
    if col not in palette:
        palette.append(col)
        count += 1
        col_str = ''.join(str(col))
        cv.putText(img, col_str, (X - 50, Y), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                   ((255 - col[0]), (255 - col[1]), (255 - col[2])), 1)
        cv.imshow("Image", img)
        cv.waitKey(100)
cv.putText(img, str(count) + " colours present", (w//2 - 100, h), cv.FONT_HERSHEY_DUPLEX, 1, (255, 0, 100), 2)
cv.imshow("Image", img)
cv.waitKey(0)
print(len(palette))

# Known Error: https://stackoverflow.com/questions/35247211/zerodivisionerror-python
