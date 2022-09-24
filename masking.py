import cv2
import numpy as np


#runs on movement of trackbar
def empty(a):
    pass

path=r'C:\Users\PRASANNA\Desktop\LearnOpenCV\lamboo.png'

#Creating Trackbar to find HSV value of certain color
cv2.namedWindow('Trackbars')
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar('Hue Min','Trackbars', 0,179,empty)
cv2.createTrackbar('Hue Max','Trackbars',179,179,empty)
cv2.createTrackbar('Sat Min','Trackbars',10,255,empty)
cv2.createTrackbar('Sat Max','Trackbars',255,255,empty)
cv2.createTrackbar('Val Min','Trackbars',170,255,empty)
cv2.createTrackbar('Val Max','Trackbars',255,255,empty)
img=cv2.imread(path)
img1=cv2.resize(img,(200,200))


while(True):
   
    img_hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
    h_min=cv2.getTrackbarPos("Hue Min","Trackbars")
    h_max=cv2.getTrackbarPos("Hue Max","Trackbars")
    s_min=cv2.getTrackbarPos("Sat Min","Trackbars")
    s_max=cv2.getTrackbarPos("Sat Max","Trackbars")
    v_min=cv2.getTrackbarPos("Val Min","Trackbars")
    v_max=cv2.getTrackbarPos("Val Max","Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    mask=cv2.inRange(img_hsv,lower,upper)
    imgResult=cv2.bitwise_and(img1,img1,mask=mask)

    

    print(mask.shape)

# cv2.imshow('lambo',img)
    cv2.imshow('final',mask)
    finall=np.hstack((img1,imgResult))
    cv2.imshow("om",finall)
    cv2.waitKey(1)
