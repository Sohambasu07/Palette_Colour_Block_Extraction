import numpy as np
import cv2 as cv
import math
print("Enter Hue Value: ")
h=int(input())
print("Enter size of color blocks: ")
s=int(input())


def create_color(x, y):
    col = [h, x, y]
    a = [[col]*s]*s
    #print(a)
    a = np.array(a, np.uint8)
    img = cv.cvtColor(a, cv.COLOR_BGR2HSV)
    print(img)
    cv.imshow("Image", img)
    cv.waitKey(5000)


x=255
y=255
create_color(x,y)
