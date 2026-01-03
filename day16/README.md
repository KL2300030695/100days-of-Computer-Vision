# Day 16: Live Face Detection

## Task
Implement live face detection using OpenCV.

## Approach
- Loaded a Haar Cascade face detection model.
- Accessed the webcam for live video input.
- Converted frames to grayscale for detection.
- Detected faces using Haar Cascade classifier.
- Drew bounding boxes around detected faces.
- Displayed results in real time.

## Techniques Used
- `cv2.CascadeClassifier()` – Load Haar model
- `detectMultiScale()` – Face detection
- `cv2.VideoCapture()` – Webcam access
- `cv2.rectangle()` – Draw bounding boxes

## Insights and Challenges
- Haar cascades require grayscale images.
- Detection accuracy depends on lighting and scale.
- This method is fast and suitable for real-time use.

## Code
Implementation is available in `day16.py`.
