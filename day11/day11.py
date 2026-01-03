import cv2
import os

# -----------------------------
# Build image path safely
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, "..", "images", "day6.jpg")

print("Image path:", image_path)
print("Exists:", os.path.exists(image_path))

# -----------------------------
# Load Image
# -----------------------------
image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Could not load image")
    exit()

print("✅ Image loaded successfully")

# -----------------------------
# Apply Gaussian Blur
# -----------------------------
# Kernel size must be odd
kernel_size = (5, 5)

# sigmaX = 0 lets OpenCV calculate it automatically
gaussian_blurred = cv2.GaussianBlur(image, kernel_size, sigmaX=0)

# -----------------------------
# Display Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", gaussian_blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
