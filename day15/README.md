# Day 15: Mouse Event as a Paint Brush

## Task
Use mouse events to draw on a live camera feed, simulating a paint brush.

## Approach
- Captured live video from the webcam.
- Created a blank drawing canvas.
- Used mouse callback functions to track drawing.
- Drew lines based on mouse movement.
- Combined the canvas with the live video feed.

## Controls
- Left Mouse Button: Draw
- Press 'c': Clear drawing
- Press 'q': Quit application

## Techniques Used
- `cv2.setMouseCallback()` – Mouse event handling
- `cv2.VideoCapture()` – Live camera feed
- `cv2.line()` – Drawing
- `cv2.add()` – Overlay drawing on video

## Insights and Challenges
- Mouse callbacks are event-driven.
- Canvas overlay allows persistent drawing.
- Useful for interactive CV applications.

## Code
Implementation is available in `day15.py`.
