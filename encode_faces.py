import face_recognition
import os
import pickle
import cv2

dataset_path = "Dataset"
known_encodings = []
known_names = []

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    
    for image_name in os.listdir(person_path):
        image_path = os.path.join(person_path, image_name)
        image = cv2.imread(image_path)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        boxes = face_recognition.face_locations(rgb, model="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person)

# Save encodings
data = {"encodings": known_encodings, "names": known_names}
with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("[INFO] Encodings generated and saved to encodings.pickle")
