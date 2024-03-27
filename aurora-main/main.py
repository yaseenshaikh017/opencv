
def detect_face(self):
    prev_time = 0  # Initialize prev_time here
    while True:
        ret, frame = self.cap.read()
        if frame is None:
            print("No frame detected! ")
        else:
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            haar_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt.xml')
            faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=9, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
            for (x, y, w, h) in faces_rect:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
            
            if len(faces_rect) > 0 and not self.time_started:
                prev_time = int(time.time())  # Set prev_time only when faces are detected
                self.take_snapshot(frame)
            
            curr_time = int(time.time())
            if self.time_started:
                if curr_time - prev_time > 5:
                    self.time_started = False
                    cv2.destroyAllWindows()
        
        cv2.imshow("", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Closing the camera
            break

    self.cap.release()
    cv2.destroyAllWindows()  # It destroys all the windows and closes the app
