import cv2
import os

# -----------------------------
# Load Image (Safe Absolute Path)
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, "..", "images", "day6.jpg")

image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Could not load image")
    exit()

print("✅ Image loaded successfully")

# -----------------------------
# Apply Median Blur
# -----------------------------
kernel_size = 5  # must be odd
median_blurred = cv2.medianBlur(image, kernel_size)

# -----------------------------
# Display Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Median Blurred Image", median_blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
