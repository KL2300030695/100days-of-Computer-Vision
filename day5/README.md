# Day 5: Drawing Circle on Live Camera Feed

## Task
Draw a circle on a live camera feed in real-time.

## Approach
- Accessed the system webcam using OpenCV.
- Captured video frames continuously.
- Calculated the center of each frame.
- Drew a circle at the center using OpenCV drawing functions.
- Displayed the processed frames in real-time.

## Techniques Used
- `cv2.VideoCapture()` – Access webcam
- `cap.read()` – Capture video frames
- `cv2.circle()` – Draw circle
- `cv2.imshow()` – Display frames
- `cv2.waitKey()` – Keyboard interaction

## Insights and Challenges
- Real-time processing requires efficient frame handling.
- Drawing operations must be applied to each frame.
- Proper resource release is important to avoid camera lock issues.

## Code
Implementation is available in `day5.py`.
