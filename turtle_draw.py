import cv2 as cv
import numpy as np
import turtle
# read the image file

img = cv.imread('shrek.jfif', 2)
  
ret, bw_img = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
pic = np.array(bw_img)
cursor = turtle.Pen()
for i in range(pic.shape[0]):
    for j in range(pic.shape[1]):
        if pic[i,j] == 255:
            cursor.penup()
        else:
            cursor.pendown()
        cursor.fd(1)
        if j == pic.shape[1]-1:
            cursor.penup()
            cursor.goto(0,-(i+1))
        
