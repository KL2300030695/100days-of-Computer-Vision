# Day 11: OpenCV Gaussian Blur

## Task
Apply Gaussian blur to an image using OpenCV.

## Input
Image file: images/day6.jpg

## Approach
- Loaded the input image.
- Applied Gaussian blur with a fixed kernel size.
- Displayed the original and blurred images.

## Techniques Used
- `cv2.imread()` – Load image
- `cv2.GaussianBlur()` – Gaussian smoothing
- `cv2.imshow()` – Display output

## Insights and Challenges
- Gaussian blur weights nearby pixels more heavily.
- Kernel size controls the level of smoothing.
- Useful as a preprocessing step before edge detection and feature extraction.

## Code
Implementation is available in `day11.py`.
