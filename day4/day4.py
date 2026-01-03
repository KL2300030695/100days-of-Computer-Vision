import cv2
import os
import numpy as np

# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to grayscale image from Day 3
gray_image_path = os.path.join(BASE_DIR, "..", "day3", "grayscale_image.png")

print("Grayscale image path:", gray_image_path)
print("Exists:", os.path.exists(gray_image_path))

# Load grayscale image
gray = cv2.imread(gray_image_path, cv2.IMREAD_GRAYSCALE)

if gray is None:
    print("❌ Error: Could not load grayscale image")
    exit()

print("✅ Grayscale image loaded")

# ----------------------------------
# Background Removal using Threshold
# ----------------------------------

# Otsu Thresholding
_, binary = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Morphological opening to remove noise
kernel = np.ones((3, 3), np.uint8)
clean_mask = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

# Extract foreground
foreground = cv2.bitwise_and(gray, gray, mask=clean_mask)

# Save output
output_path = os.path.join(BASE_DIR, "background_removed.png")
cv2.imwrite(output_path, foreground)

print("✅ Background removed image saved at:", output_path)

# ----------------------------------
# Display results
# ----------------------------------
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Binary Mask", clean_mask)
cv2.imshow("Background Removed", foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()
