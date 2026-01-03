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
# Apply Bilateral Filter
# -----------------------------
# d = Diameter of pixel neighborhood
# sigmaColor = Filter sigma in color space
# sigmaSpace = Filter sigma in coordinate space
bilateral_filtered = cv2.bilateralFilter(
    image,
    d=9,
    sigmaColor=75,
    sigmaSpace=75
)

# -----------------------------
# Display Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Bilateral Filtered Image", bilateral_filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()
