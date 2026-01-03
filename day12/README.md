# Day 12: OpenCV Bilateral Filter

## Task
Implement a bilateral filter on an image using OpenCV.

## Input
Image file: images/day6.jpg

## Approach
- Loaded the input image using a safe relative path.
- Applied bilateral filtering to smooth the image.
- Preserved edges while reducing noise.
- Displayed original and filtered images.

## Techniques Used
- `cv2.imread()` – Load image
- `cv2.bilateralFilter()` – Edge-preserving smoothing
- `cv2.imshow()` – Display images

## Insights and Challenges
- Bilateral filtering preserves edges unlike Gaussian blur.
- Parameter tuning is important for best results.
- Computationally more expensive than other blurs.

## Code
Implementation is available in `day12.py`.
