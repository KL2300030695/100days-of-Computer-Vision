# Day 8: Canny Edge Detection on Live Video Feed

## Task
Apply Canny edge detection to a live camera feed.

## Approach
- Accessed the webcam using OpenCV.
- Converted each video frame to grayscale.
- Applied Gaussian blur to reduce noise.
- Performed Canny edge detection.
- Displayed both the original and edge-detected frames in real-time.

## Techniques Used
- `cv2.VideoCapture()` – Webcam access
- `cv2.cvtColor()` – Grayscale conversion
- `cv2.GaussianBlur()` – Noise reduction
- `cv2.Canny()` – Edge detection
- `cv2.imshow()` – Real-time display

## Insights and Challenges
- Noise reduction is critical for stable edge detection.
- Threshold values affect edge sensitivity.
- Real-time processing requires efficient operations.

## Code
Implementation is available in `day8.py`.
