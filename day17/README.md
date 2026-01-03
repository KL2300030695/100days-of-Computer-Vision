# Day 17: Facial Recognition Implementation

## Task
Implement facial recognition using OpenCV and face_recognition library.

## Approach
- Loaded a known face image and extracted its facial encoding.
- Captured live video from webcam.
- Detected faces in each frame.
- Compared detected face encodings with known encodings.
- Displayed the recognized person's name in real time.

## Techniques Used
- `face_recognition.face_encodings()` – Face feature extraction
- `face_recognition.compare_faces()` – Face matching
- `face_recognition.face_distance()` – Similarity measurement
- `cv2.VideoCapture()` – Live camera feed
- `cv2.rectangle()` – Bounding box
- `cv2.putText()` – Label annotation

## Insights and Challenges
- Face recognition requires RGB images.
- Image quality greatly affects recognition accuracy.
- Face distance improves match reliability over boolean comparison.

## Code
Implementation is available in `day17.py`.
