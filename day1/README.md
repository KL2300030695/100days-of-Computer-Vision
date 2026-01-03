# Day 1: Camera Image Capture

## Task
Load an image from the camera and save it to the local directory.

## Approach
- Used OpenCV library to access the camera.
- Captured a single frame from the default camera (index 0).
- Saved the captured frame as a JPEG image in the current directory.

## Techniques Used
- `cv2.VideoCapture(0)`: To initialize video capture from the camera.
- `cap.read()`: To capture a frame.
- `cv2.imwrite()`: To save the image to disk.
- Proper error handling for camera access and frame capture.

## Code
The implementation is in `day1.py`.

## Insights and Challenges
- Ensured the camera is available before attempting to capture.
- Simple and straightforward task to get started with OpenCV camera access.
- Challenge: Camera permissions or hardware availability in different environments.