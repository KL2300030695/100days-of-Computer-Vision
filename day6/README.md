# Day 6: Real-time Annotation on CV Camera Frame

## Task
Annotate the username and current date on the lower-left corner of a live camera frame.

## Approach
- Captured frames from the webcam using OpenCV.
- Retrieved the current system date dynamically.
- Added text annotation containing username and date.
- Positioned the annotation at the lower-left corner.
- Displayed the annotated frames in real-time.

## Techniques Used
- `cv2.VideoCapture()` – Webcam access
- `datetime.now()` – Fetch current date
- `cv2.putText()` – Draw text on frames
- `cv2.imshow()` – Display live video

## Insights and Challenges
- Text annotation must be applied to every frame in real-time.
- Correct coordinate selection is required for corner placement.
- This technique is useful for surveillance, logging, and AR overlays.

## Code
Implementation is available in `day6.py`.
