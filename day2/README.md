# Day 2: Image Loading and Resizing

## Task
Load an image from a file and resize it to a specific dimension.

## Approach
- Used OpenCV to load an image from a file path.
- Resized the image to 256x256 pixels using cv2.resize.
- Saved the resized image to the local directory.

## Techniques Used
- `cv2.imread()`: To load the image from disk.
- `cv2.resize()`: To change the image dimensions.
- `cv2.imwrite()`: To save the processed image.

## Code
The implementation is in `day2.py`.

## Insights and Challenges
- Specified a fixed dimension for resizing; in practice, aspect ratio preservation might be considered.
- Ensured the image loads successfully before processing.
- Built upon Day 1 by using the captured image as input.