import cv2
import face_recognition
import os
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# -----------------------------
# Load Known Face
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
known_face_path = os.path.join(
    BASE_DIR, "..", "known_faces", "subhash.jpg"
)

print("Known face path:", known_face_path)
print("Exists:", os.path.exists(known_face_path))

if not os.path.exists(known_face_path):
    print("❌ Known face image not found")
    exit()

# Load known image
known_image = face_recognition.load_image_file(known_face_path)

# 🔑 CRITICAL FIX: resize image (CNN becomes fast + reliable)
known_image = cv2.resize(known_image, (0, 0), fx=0.5, fy=0.5)

# Use CNN ONLY here (once)
known_face_locations = face_recognition.face_locations(
    known_image,
    model="cnn"
)

print("Faces found in known image:", len(known_face_locations))

if len(known_face_locations) == 0:
    print("❌ No face detected in known image")
    exit()

known_encoding = face_recognition.face_encodings(
    known_image,
    known_face_locations
)[0]

known_faces = [known_encoding]
known_names = ["Subhash Vadaparthi"]

print("✅ Known face loaded and encoded")

# -----------------------------
# Open Webcam
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Could not open camera")
    exit()

print("✅ Camera opened successfully")

# -----------------------------
# Live Face Recognition
# -----------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for speed
    small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    rgb_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(
        rgb_frame,
        model="hog"
    )

    face_encodings = face_recognition.face_encodings(
        rgb_frame,
        face_locations
    )

    for (top, right, bottom, left), face_encoding in zip(
        face_locations, face_encodings
    ):
        matches = face_recognition.compare_faces(
            known_faces,
            face_encoding,
            tolerance=0.5
        )

        name = "Unknown"

        face_distances = face_recognition.face_distance(
            known_faces,
            face_encoding
        )

        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]

        # Scale back
        top *= 2
        right *= 2
        bottom *= 2
        left *= 2

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(
            frame,
            name,
            (left, top - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Day 17 - Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
