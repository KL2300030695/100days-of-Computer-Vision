# Day 4: Image Background Removal

## Task
Remove the background from a grayscale image obtained in Day 3.

## Input
Grayscale image generated in Day 3.

## Approach
- Loaded the grayscale image.
- Applied Otsu’s thresholding to separate foreground and background.
- Used morphological opening to remove noise.
- Extracted the foreground using a binary mask.
- Saved and displayed the background-removed image.

## Techniques Used
- `cv2.threshold()` – Automatic thresholding (Otsu)
- `cv2.morphologyEx()` – Noise removal
- `cv2.bitwise_and()` – Foreground extraction
- `cv2.imwrite()` – Save output

## Insights and Challenges
- Background removal in grayscale relies on intensity separation.
- Otsu’s method works well when foreground and background have distinct intensities.
- Morphological operations help clean imperfect masks.

## Code
Implementation is available in `day4.py`.
