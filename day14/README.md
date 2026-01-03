# Day 14: Contours and Shape Detection

## Task
Implement contour detection and identify basic shapes in an image.

## Input
Image file: images/day6.jpg

## Approach
- Converted image to grayscale.
- Applied Gaussian blur to reduce noise.
- Used Otsu thresholding to obtain a binary image.
- Detected contours using OpenCV.
- Approximated contours to identify shape vertices.
- Classified shapes based on the number of vertices.
- Annotated detected shapes on the image.

## Techniques Used
- `cv2.findContours()` – Contour detection
- `cv2.approxPolyDP()` – Shape approximation
- `cv2.arcLength()` – Perimeter calculation
- `cv2.boundingRect()` – Rectangle detection
- `cv2.putText()` – Annotation

## Insights and Challenges
- Contour approximation simplifies shape detection.
- Area filtering helps remove noise.
- Aspect ratio helps distinguish squares from rectangles.

## Code
Implementation is available in `day14.py`.
