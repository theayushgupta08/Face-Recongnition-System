import face_recognition
import cv2
import pickle
import imutils

# Load encodings
data = pickle.load(open("encodings.pickle", "rb"))

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = imutils.resize(frame, width=600)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, boxes)
    names = []

    for encoding in encodings:
        matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.6)
        name = "Unknown"

        if True in matches:
            matchedIdxs = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIdxs:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            # Get the name with the highest count
            best_match = max(counts, key=counts.get)

            # Verify the match using face distance
            face_distances = face_recognition.face_distance(data["encodings"], encoding)
            best_match_index = matches.index(True)
            if face_distances[best_match_index] <= 0.6:  # Adjust threshold as needed
                name = best_match
            else:
                name = "Unknown"

        names.append(name)

    # Draw results
    for ((top, right, bottom, left), name) in zip(boxes, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        y = top - 10 if top - 10 > 10 else top + 10
        cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()