# Day 10: OpenCV Median Blur

## Task
Implement the median blur operation using OpenCV.

## Input
Image file: images/day6.jpg

## Approach
- Loaded the input image.
- Applied median blur using a fixed odd-sized kernel.
- Displayed the original and filtered images.

## Techniques Used
- `cv2.imread()` – Load image
- `cv2.medianBlur()` – Median filtering
- `cv2.imshow()` – Display results

## Insights and Challenges
- Median blur is effective for removing salt-and-pepper noise.
- Kernel size must always be odd.
- Edge details are preserved better than with averaging filters.

## Code
Implementation is available in `day10.py`.
