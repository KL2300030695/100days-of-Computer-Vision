# Day 13: Adaptive Thresholding for Pencil Sketch

## Task
Create a pencil sketch effect on a live camera feed using adaptive thresholding.

## Approach
- Captured live video frames using OpenCV.
- Converted frames to grayscale.
- Applied Gaussian blur to reduce noise.
- Used adaptive thresholding to generate a sketch-like effect.
- Displayed the result in real time.

## Techniques Used
- `cv2.VideoCapture()` – Live camera access
- `cv2.cvtColor()` – Grayscale conversion
- `cv2.GaussianBlur()` – Noise reduction
- `cv2.adaptiveThreshold()` – Pencil sketch effect
- `cv2.imshow()` – Real-time display

## Insights and Challenges
- Adaptive thresholding works well under uneven lighting.
- Block size and constant values affect sketch thickness.
- Real-time processing must be efficient.

## Code
Implementation is available in `day13.py`.
