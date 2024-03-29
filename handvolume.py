import mediapipe 
import cv2 
import time 
import numpy as np
import handtrackingmodule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume





#volume dec/incr
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange=volume.GetVolumeRange()
minVol=volRange[0]
maxVol=volRange[1]
vol=0
volBar=400
per=0

wCam,hCam=640,480
pTime=0

detector=htm.handDetector(detectionCon=0.7)


cap=cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)

while True:
    success,img=cap.read()
    img=detector.findHands(img)
    lmList=detector.findPosition(img,draw=False)
    if len(lmList) !=0:
            # print(lmList[4],lmList[8])
            x1,y1=lmList[4][1],lmList[4][2]
            x2,y2=lmList[8][1],lmList[8][2]
            cx,cy=(x1+x2)//2,(y1+y2)//2

            cv2.circle(img,(x1,y1),15,(255,0,255),cv2.FILLED)
            cv2.circle(img,(x2,y2),15,(255,0,255),cv2.FILLED)
            cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
            cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)

            length=math.hypot(x2-x1,y2-y1)
            
            #5-231
            #-65-0
            vol=np.interp(length,[5,231],[minVol,maxVol])
            volBar=np.interp(length,[5,231],[400,150])
            per=np.interp(length,[5,231],[0,100])

            volume.SetMasterVolumeLevel(vol, None)



            if length<50:
                 cv2.circle(img,(cx,cy),15,(0,255,0),cv2.FILLED)
    
    cv2.putText(img,f'{str(per)} %',(40,90),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
    cv2.rectangle(img,(50,100),(85,400),(255,0,0),3,cv2.FILLED)
    cv2.rectangle(img,(50, int(volBar)),(85,400),(255,0,0),-1)

                 


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,f'fps:{str(int(fps))}',(40,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
    

    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break