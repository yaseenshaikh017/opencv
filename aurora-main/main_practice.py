import cv2
import time

# scaleFactor – This tells how much the object’s size is reduced to the original image.
# minNeighbors – This parameter tells how many neighbors should contribute in a single bounding box.
# minSize — This signifies the minimum possible size of the object in our image. if our object is smaller than the minSize it will be ignored.



class selfie:

    def __init__(self):

        self.cap=cv2.VideoCapture(0)
        self.time_started = False
        self.count=1
        self.detect_face()
        

    def take_snapshot(self,frame):
        
        self.time_started=True
        print("Press s to save the image")
        ch =  cv2.waitKey(3000)  #3000ms
        if ch==ord('s'):
            cv2.imwrite(str(self.count)+'.jpg',frame)
            self.count=self.count+1
            print("saved")
        
        def detect_face(self):
            
            while True:
                ret,frame=self.cap.read()
                
                if frame is None:
                    print("No frame detected")
                    
                else:
                    gray_img=cv2.cvtcolor(frame,cv2.COLOR_BGR2GRAY) 
                    haar_cascade=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_alt.xml")
                       faces_rect =  haar_cascade.detectMultiScale()