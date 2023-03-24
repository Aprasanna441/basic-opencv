import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

while True:
    _,frame=cap.read()
    
    blurred_frame=cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
    arra=np.array([127,101,0,179,255,255])
    lower=np.array(arra[0:3])
    upper=np.array(arra[3:6])
    mask=cv2.inRange(hsv,lower,upper)
    contours,_= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    

    for contour in contours:
       area=cv2.contourArea(contour)
       if(area>1000):
          cv2.drawContours(frame,contour,-1,(0,255,0),3)
          x,y,w,h = cv2.boundingRect(contour)
          cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0,255), 2)
          
            
   


    cv2.imshow("frame",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cv2.release()
