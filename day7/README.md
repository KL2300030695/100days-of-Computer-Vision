# Day 7: Blob Analysis by Convexity

## Task
Perform blob analysis using the convexity feature on an input image.

## Input
Image file: images/day6.jpg

## Approach
- Converted the image to grayscale.
- Applied Otsu’s thresholding to obtain a binary image.
- Detected blobs using contour extraction.
- Computed convex hulls for each blob.
- Calculated convexity as the ratio of blob area to hull area.
- Visualized contours, convex hulls, and convexity values.

## Techniques Used
- `cv2.findContours()` – Blob detection
- `cv2.convexHull()` – Convex hull computation
- `cv2.contourArea()` – Area calculation
- `cv2.putText()` – Annotation

## Insights and Challenges
- Convexity helps differentiate regular and irregular objects.
- Small contours should be filtered to remove noise.
- Convex hulls provide geometric robustness in blob analysis.

## Code
Implementation is available in `day7.py`.
