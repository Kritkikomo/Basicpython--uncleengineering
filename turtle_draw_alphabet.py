import turtle
import cv2 as cv
import numpy as np
def read_alphabet(alphabet):
    alphabet_lst=np.array([['a','b','c','d','e','f'],['g','h','i','j','k','l'],
                       ['m','n','o','p','q','r'],['s','t','u','v','w','x'],
                       [' ', 0,'y','z',0,0]])
    img = cv.imread('army-alphabet-chart.jpg')
    #print(img.shape) # Print image shape
    #cv.imshow("original", img)
    
    alph_index = np.where(alphabet_lst== alphabet)
    alph_pos =[104+121*int(alph_index[1]),131+121*int(alph_index[1]),105+65*int(alph_index[0]),130+65*int(alph_index[0])]
    cropped_image = img[alph_pos[2]:alph_pos[3], alph_pos[0]:alph_pos[1]]
    ret, bw_img = cv.threshold(cropped_image, 127, 255, cv.THRESH_BINARY)
    return bw_img
def writ_alph_tur(string):
    cursor = turtle.Pen()
    cursor.right(90)
    current_pos=0
    j=0
    for x in string:
        bw_img=read_alphabet(x)
        pic = np.array(bw_img)
        cursor.goto(j+current_pos,0)
        for j in range(pic.shape[1]):
            for i in range(pic.shape[0]):
                if pic[i,j,0] == 255:
                    cursor.penup()
                else:
                    cursor.pendown()
                cursor.fd(1)
                if i == pic.shape[0]-1:
                    cursor.penup()
                    cursor.goto(j+1+current_pos,0)
        current_pos+=j
writ_alph_tur('uncle engineer')
'''space  x =121 y=65
row(0,0) =[104:131,105:130]
A=[104:131, 105:130]
B=[102:130, 226:251]
C=[102:130, 350:370]
D =[102:130, 471:491]
E= [102:130, 592:612]
F= 102:130, 713:733]
G =[170:195, 105:130]'''
# Cropping an image
    
# Display cropped image
    

    
