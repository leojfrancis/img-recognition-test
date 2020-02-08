# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 04:49:20 2020

@author: DELL
"""

import cv2
import numpy as np
import os 
import pytesseract
import matplotlib.pyplot as plt
%matplotlib inline

def plot_imgs(img1,img2,title1="",title2=""):
    fig=plt.figure(figsize=[15,15])
    
    axl=fig.add_subplot(121)
    axl.imshow(img1,cmap="gray")
    axl.set(xticks=[],yticks=[],title=title1)
    
    ax2=fig.add_subplot(122)
    ax2.imshow(img1,cmap="gray")
    ax2.set(xticks=[],yticks=[],title=title2)
    
path = r"C:\Users\DELL\Downloads\car2.jpg"
image=cv2.imread(path)
plot_imgs(image,image,title1="orginal",title2="original")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plot_imgs(image,gray,title1="orginal",title2="gray")

blur=cv2.bilateralFilter(gray,11,90,90)
plot_imgs(gray,blur,title1="gray",title2="blur")

edges=cv2.Canny(blur,30,200)
plot_imgs(blur,edges,title1="blur",title2="edges")
cnts,new=cv2.findContours(edges.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

type(cnts)
print(cnts[0])

image_copy=image.copy()
#print(image_copy)

_=cv2.drawContours(image_copy,cnts,-1,(255,0,255),3)
#print(_)
plot_imgs(edges,image_copy,title1="edges",title2="Contours")

print(len(cnts))

cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:30]
#print(cnts)
image_reduced_cnts=image.copy()
_=cv2.drawContours(image_reduced_cnts,cnts,-1,(255,0,255),3)
plot_imgs(image_copy,image_reduced_cnts,title1="contours",title2="Reduced")

#print(len(cnts))
plate=None
for c in cnts:
    perimeter=cv2.arcLength(c,True)
    edges_cnts=cv2.approxPolyDP(c,0.02*perimeter,True)
    if len(edges_cnts) == 4:
        x,y,w,h=cv2.boundingRect(c)
        plate=image[y:y+h,x:x+w]
        print(plate)
        break
cv2.imwrite("plate.png",plate)    

plot_imgs(plate,plate,title1="plate",title2="plate")
    
        
        

