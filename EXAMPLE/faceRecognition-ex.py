
import face_recognition
import cv2
import numpy as np
import os
import time
import random
"""
# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\haarcascade_frontalface_default.xml')

# Load functions
def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+300, x:x+300]

    return cropped_face

# Initialize Webcam
cap = cv2.VideoCapture(0)
count = 0

# Collect 100 samples of your face from webcam input
while True:

    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (400, 400))
        #face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

        # Save file in specified directory with unique name
        file_name_path = r"D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\images\img" + str(count) + ".JPG"
        cv2.imwrite(file_name_path, face)

        # Put count on images and display live count
        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
        cv2.imshow('Face Cropper', face)
        
    else:
        print("Face not found")
        pass

    if cv2.waitKey(1) == 13 or count == 100 : #13 is the Enter Key
        break
        
cap.release()
cv2.destroyAllWindows()      
print("Collecting Samples Complete")
"""

"""
####clicking picture ####


import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

def faceDetection(test_img):
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    face_haar_cascade = cv2.CascadeClassifier("D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\haarcascade_frontalface_default.xml")
    face = face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)
    return face, gray_img



while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)
  
    if img_counter==100:
        #k = cv2.waitKey(1)
        print("Escape hit, closing...")
        break
    else:
        file_name_path = r"D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\images\img" + str(img_counter) + ".png"
        cv2.imwrite(file_name_path,frame)
        print("captured")
        img_counter += 1    

cam.release()
cv2.destroyAllWindows


        Test_img = cv2.imread(file_name_path)
        faceDetected , Gray_img = faceDetection(Test_img)
        print("facedetected: ",faceDetected)

        for (x,y,w,h) in faceDetected:
            cv2.rectangle(Test_img,(x,y),(x+w,y+h),(0,255,0),thickness=3)

        resize_img=cv2.resize(Test_img,(1000,700))
        cv2.imshow("test",resize_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows

"""

"""

def faceDetection(test_img):
    gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
    face_haar_cascade = cv2.CascadeClassifier("D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\haarcascade_frontalface_default.xml")
    face = face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=5)
    return face, gray_img

def labels_for_training_data(directory):
    faces=[]
    faceId=[]

    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."):
                print("skipping")
                continue

            Id = os.path.basename(path)
            img_path = os.path.join(path,filename)
            print("img_path: ",img_path)
            print("id : ",Id)
            test_img=cv2.imread(img_path)
            if test_img is None:
                print("image not loaded")
                continue
            faces_rect, gray_img = faceDetection(test_img)
            if len(faces_rect)!=1:
                continue #single person face
            (x,y,w,h)=faces_rect[0]
            roi_gray = gray_img[y:y+w,x:x+h]
            faces.append(roi_gray)
            faceId.append(int(Id))
    return faces,faceId

def train_classifier(faces,faceId):
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.train(faces, np.array(faceId))
    return face_recognizer

def draw_rect(test_img,face):
    (x,y,w,h) = face 
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,5,(255,0,0),6)





Test_img = cv2.imread("D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\IMG_20181015_163004.jpg")
faceDetected , Gray_img = faceDetection(Test_img)
print("facedetected: ",faceDetected)


#for (x,y,w,h) in faceDetected:
#    cv2.rectangle(Test_img,(x,y),(x+w,y+h),(0,255,0),thickness=3)

#resize_img=cv2.resize(Test_img,(1000,700))
#cv2.imshow("test",resize_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows
#faces , faceId = labels_for_training_data("D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\images")
#face_recognizer = train_classifier(faces,faceId)
#face_recognizer.save("trainData.yml")

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read("trainData.yml")
name = {0:"raju"}

for face in faceDetected:
    (x,y,w,h)=face 
    roi_gray = Gray_img[y:y+h,x:x+h]
    label,confidence=face_recognizer.predict(roi_gray)
    print("confidence: ",confidence)
    print("label: ",label)
    if confidence < 60:
        draw_rect(Test_img,face)
        predicted_name = name[label]
        put_text(Test_img,predicted_name,x,y)

resize_img=cv2.resize(Test_img,(1000,700))
cv2.imshow("face_detected",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows
"""

#### face recognition using face_recognition libary in image -- sentdex####
"""
KNOWN_FACE_DIR = "KNOWN_FACE"
UNKNOWN_FACE_DIR = "UNKNOWN_FACE"

TOLLERANCE = 0.4
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn" 

print("loading known faces")

known_faces = []
known_names = []

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

print("taking picture ")


cam = cv2.VideoCapture(0)

#cv2.namedWindow("click picture")

#img_counter = 0

while True:
    k=cv2.waitKey(1)
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        print("failed to grab frame")
        break
    #cv2.imshow("test", frame)
  
    #if img_counter==1:
        #k = cv2.waitKey(1)
        #print("Escape hit, closing...")
        #break
    if k%256==32:
        img = random.randint(1,1000000)
        file_name_path = r"D:\CODE_STORAGE\PYTHON\PYCODES\JARVIS\UNKNOWN_FACE\img" + str(img) + ".png"
        scale_percent = 50 # percent of original size
        width = int(frame.shape[1] * scale_percent / 100)
        height = int(frame.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized_frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        cv2.imwrite(file_name_path,resized_frame)
        print("captured")
        break
        #img_counter += 1    

cam.release()
cv2.destroyAllWindows()

print("processing unknown faces")


for filename in os.listdir(UNKNOWN_FACE_DIR):
    print(filename)
    image = face_recognition.load_image_file(f"{UNKNOWN_FACE_DIR}\{filename}")
    face_locations = face_recognition.face_locations(image, model=MODEL)  
    encodings = face_recognition.face_encodings(image,face_locations)
    image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
        
    for face_encoding, face_location in zip(encodings, face_locations):
        results = face_recognition.compare_faces(known_faces,face_encoding,TOLLERANCE)
        match = None

        
        if True in results:
            match = known_names[results.index(True)]
                
            print(f"Match found: {match}")
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
            print("match not found")
        
    cv2.imshow(filename, image)
    cv2.waitKey(10000)
    #cv2.destroyAllWindows            
"""

"""
#### face recognition using face_recognition libary in video -- sentdex####

KNOWN_FACE_DIR = "KNOWN_FACE"
#UNKNOWN_FACE_DIR = "UNKNOWN_FACE"

video= cv2.VideoCapture(0)

TOLLERANCE = 0.5
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = "cnn" 

print("loading known faces")

known_faces = []
known_names = []

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

print("processing unknown faces")
while True:

    ret, image=video.read()

    face_locations = face_recognition.face_locations(image, model=MODEL)  
    encodings = face_recognition.face_encodings(image,face_locations)
    #image = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)
            
    for face_encoding, face_location in zip(encodings, face_locations):
        results = face_recognition.compare_faces(known_faces,face_encoding,TOLLERANCE)
        match = None

            
        if True in results:
            match = known_names[results.index(True)]
                
            print(f"Match found: {match}")
                    #face_names.append(name)

        
            
            top_left = (face_location[3], face_location[0])
            bottom_right = (face_location[1],face_location[2])
            color = [0,0,255]
            cv2.rectangle(image, top_left,bottom_right,color,FONT_THICKNESS)
                    
            top_left = (face_location[3], face_location[2])
            bottom_right = (face_location[1],face_location[2]+22)
            cv2.rectangle(image, top_left,bottom_right,color,cv2.FILLED)
            cv2.putText(image,match,(face_location[3]+10,face_location[2]+15),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,200,200),FONT_THICKNESS)
            
            
    cv2.imshow(filename, image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        #cv2.destroyAllWindows   
"""
