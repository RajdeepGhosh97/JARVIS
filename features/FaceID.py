# # # FACE-RECOGNITION # # # 
import face_recognition
import cv2
import numpy as np
import os
import random

# # # CUSTOM-MADE IMPORTS # # #
from ListenSpeak import speak , myCommand




# # # FACE-RECOGNITION KNOWN-FACE LOADING  # # #
KNOWN_FACE_DIR = "KNOWN_FACE"
UNKNOWN_FACE_DIR = "UNKNOWN_FACE"
TOLLERANCE = 0.4
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn" 
known_faces = []
known_names = []  
speak("loading faces")
for name in os.listdir(KNOWN_FACE_DIR):
    for filename in os.listdir(f"{KNOWN_FACE_DIR}\{name}"):
        image = face_recognition.load_image_file(f"{KNOWN_FACE_DIR}\{name}\{filename}")
        encodings = face_recognition.face_encodings(image)
        if len(encodings) > 0:
            encoding = encodings[0]
        else:
            print("No faces found in the image! in ",filename)
            continue
        known_faces.append(encoding)
        known_names.append(name)



def click_pic():
    cam = cv2.VideoCapture(0)
    speak(" press space-bar to capture image ")
    while True:
        k=cv2.waitKey(1)
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            print("failed to grab frame")
            break
        if k%256==32:
            #cv2.destroyWindow('test') 
            img = random.randint(1,1000000)
            file_name_path = r"D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\UNKNOWN_FACE\img" + str(img) + ".png"
            scale_percent = 50 # percent of original size
            width = int(frame.shape[1] * scale_percent / 100)
            height = int(frame .shape[0] * scale_percent / 100)
            dim = (width, height)
            resized_frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(file_name_path,resized_frame)
            print("captured")
            break    

    cam.release()
    cv2.destroyAllWindows()
    return file_name_path


def process_face(file_name):
    speak("FACE VERIFICATION UNDER PROCESS")
    #for filename in os.listdir(UNKNOWN_FACE_DIR):
    FILE = file_name
    print(FILE)
    image = face_recognition.load_image_file(FILE)
    face_locations = face_recognition.face_locations(image, model=MODEL)  
    encodings = face_recognition.face_encodings(image,face_locations)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

    speak("COMPARING YOUR FACE WITH THE DATABASE ")    
    for face_encoding, face_location in zip(encodings, face_locations):
        results = face_recognition.compare_faces(known_faces,face_encoding,TOLLERANCE)
        match = None

            
        if True in results:
            match = known_names[results.index(True)]
                    
            print(f"Match found: {match}")
                #speak("match found")
                #speak(f"welcome {match} ")
                #face_names.append(name)
            
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1],face_location[2])
            color = [0,0,255]
            cv2.rectangle(image, top_left,bottom_right,color,FONT_THICKNESS)
                    
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1],face_location[2]+22)
            cv2.rectangle(image, top_left,bottom_right,color,cv2.FILLED)
            cv2.putText(image,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,200,200),FONT_THICKNESS)
        else:
            match = "unknown"
            print("match not found")
            #speak("match not found")
        
    #cv2.imshow(filename, image)
    #cv2.waitKey(10000)
    #cv2.destroyAllWindows
    return match