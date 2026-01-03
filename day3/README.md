# Day 3: Loading and Grayscale Conversion

## Task
Load an image from a URL and convert it to grayscale.

## Image Source
https://github.com/AIBauchi/.github/blob/main/profile/image.png

## Approach
- Downloaded the image directly from a URL.
- Decoded the image using OpenCV.
- Converted the color image to grayscale.
- Displayed both original and grayscale images.
- Saved the grayscale image to disk.

## Techniques Used
- `urllib.request.urlopen()` – Fetch image from URL
- `cv2.imdecode()` – Decode image bytes
- `cv2.cvtColor()` – Convert BGR to grayscale
- `cv2.imwrite()` – Save processed image

## Insights and Challenges
- Images from URLs must be decoded before OpenCV processing.
- Grayscale conversion reduces computational complexity.
- This step is essential for edge detection and segmentation tasks.

## Code
Implementation is available in `day3.py`.
