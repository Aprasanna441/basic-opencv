import cv2 
import mediapipe as mp 

import time
mpPose=mp.solutions.pose 
pose=mpPose.Pose()
mpDraw=mp.solutions.drawing_utils

class poseDetector():

    def __init__(self,mode=False,complexity=1,smooth=True,enable=False,smoothseg=True,detectionCon=0.5,trackCon=0.2):
        self.mode=mode
        self.complexity=complexity
        
        self.smooth=smooth
        self.enable=enable
        self.smoothseg=smoothseg
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpPose=mp.solutions.pose 
        self.pose=self.mpPose.Pose(self.mode,
                                   self.complexity,self.smooth,
                                   self.enable,self.smoothseg,self.detectionCon,self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils

        

    def findPose(self,img,draw=True):
        imgrgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.pose.process(imgrgb)
        if self.results.pose_landmarks:
              if draw:
                    self.mpDraw.draw_landmarks(img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
        
        return img
    
    def findPosition(self,img,draw=True):
        lmList=[]
        for id,lm in enumerate(self.results.pose_landmarks.landmark): 
          if self.results.pose_landmarks:
             h,w,c=img.shape
           
             cx,cy=int(lm.x*w),int(lm.y*h)
             lmList.append([id,cx,cy])
            
             if draw:
                  
                  cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)     

        return lmList
              
              
         



        
         
        





    
    
        # 
        #     h,w,c=img.shape
           
        #     cx,cy=int(lm.x*w),int(lm.y*h)
        #     print(id,cx,cy)
        #     cv2.circle(img,(cx,cy),5,(255,0,0),cv2.FILLED)

        

    


   

def main():
    cap=cv2.VideoCapture(0)
    pTime=0
    detector=poseDetector()
    while True:
        success,img=cap.read()
        
        img=detector.findPose(img)
        lmList=detector.findPosition(img,draw=False)
        if len(lmList)!=0:
             print(lmList[14] )
             cv2.circle(img,(lmList[14][1],lmList[14][2]),10,(0,0,255),cv2.FILLED) 


         

        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        cv2.imshow("image",img)

        if cv2.waitKey(1) & 0XFF==ord('q'):
              break


    

if __name__=="__main__":
    main()