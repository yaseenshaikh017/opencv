import cv2
import mediapipe as mp

#how are faces getting detected?

# Collection of detected faces, where each face is represented as a detection proto message that contains a bounding box 
# and 6 key points (right eye, left eye, nose tip, mouth center, right ear tragion, and left ear tragion). 
# The bounding box is composed of xmin and width (both normalized to [0.0, 1.0] by the image width) and 
# ymin and height (both normalized to [0.0, 1.0] by the image height). Each key point is composed of x and y, 
# which are normalized to [0.0, 1.0] by the image width and height respectively.



# model_selection:
# Use 0 to select a short-range model that works best for faces within 2 meters from the camera, 
# and 1 for a full-range model best for faces within 5 meters.

# min_detection_confidence:
# Minimum confidence value ([0.0, 1.0]) 
# from the face detection model for the detection to be considered successful. Default to 0.5

mp_drawing = mp.solutions.drawing_utils
# load face detection model
mp_face = mp.solutions.face_detection.FaceDetection(
    model_selection=1, # model selection
    min_detection_confidence=0.8 # confidence threshold

)

cap=cv2.VideoCapture(0)

while True:

    ret,frame=cap.read()
    image_input = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # get results
    results = mp_face.process(image_input)

    if not results.detections:
        print('No faces detected.')
    else:
        for detection in results.detections: # iterate over each detection and draw on image
            mp_drawing.draw_detection(frame, detection)

    cv2.imshow("",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
cap.release()
cv2.destroyAllWindows()