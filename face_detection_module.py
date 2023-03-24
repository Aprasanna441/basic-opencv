import cv2 
import mediapipe as mp 
import time
import math

class faceDetection():
    def __init__(self,minDetectionCon=0.5,model_selection=1):
        self.model_selection=model_selection
        self.minDetectionCon=minDetectionCon


        self.mpFaceDetection=mp.solutions.face_detection 
        self.mpDraw=mp.solutions.drawing_utils 
        self.faceDetection=self.mpFaceDetection.FaceDetection(0.75)


    def findFaces(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        self.results=self.faceDetection.process(imgRGB)
        bounding_boxes=[]
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
                bboxC=detection.location_data.relative_bounding_box
               

                ih,iw,ic=img.shape 
                bounding_box=int(bboxC.xmin*iw),int(bboxC.ymin*ih),\
                    int(bboxC.width*iw),int(bboxC.height*iw)
                bounding_boxes.append([id,bounding_box,detection.score])
                img=self.draw(img,bounding_box)
                
                cv2.putText(img,f'{int(detection.score[0]*100)}%',(bounding_box[0],bounding_box[1]-20),
                              cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)



        return img,bounding_boxes
    
   

    def draw(self,img,bbox,l=30,t=10):
        x,y,w,h=bbox
        x1,y1=x+w,y+h
        
        cv2.line(img,(x,y),(x+l,y),(0,0,255),t)
        cv2.line(img,(x,y),(x,y+l),(0,0,255),t)

        cv2.line(img,(x1,y),(x1-l,y),(0,0,255),t)
        cv2.line(img,(x1,y),(x1,y+l),(0,0,255),t)

        cv2.line(img,(x,y1),(x+l,y1),(0,0,255),t)
        cv2.line(img,(x,y1),(x,y1-l),(0,0,255),t)

        cv2.line(img,(x1,y1),(x1-l,y1),(0,0,255),t)
        cv2.line(img,(x1,y1),(x1,y1-l),(0,0,255),t)

        
        return img






def main():
    pTime=0
    cTime=0
    cap=cv2.VideoCapture(0)
    detector=faceDetection()

    while True:        
        success,img=cap.read()
        img,boundary_boxes=detector.findFaces(img)

        
       
        



        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img,f'FPS:{int(fps)}',(10,70),cv2.FONT_HERSHEY_PLAIN,3, (0,0,255),2)
        cv2.imshow("image",img)

        if (cv2.waitKey(1) & 0XFF==ord('q')):
            break
        

if __name__=="__main__":
    main()