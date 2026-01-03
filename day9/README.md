# Day 9: OpenCV Averaging (Image Smoothing)

## Task
Perform image smoothing using OpenCV averaging.

## Input
Image file: images/day6.jpg

## Approach
- Loaded the input image using OpenCV.
- Applied an averaging (mean) filter using a fixed kernel size.
- Displayed the original and smoothed images for comparison.

## Techniques Used
- `cv2.imread()` – Load image
- `cv2.blur()` – Averaging filter
- `cv2.imshow()` – Display images

## Insights and Challenges
- Averaging reduces noise but also blurs edges.
- Larger kernel sizes produce stronger smoothing.
- This technique is commonly used as a preprocessing step before edge detection.

## Code
Implementation is available in `day9.py`.
