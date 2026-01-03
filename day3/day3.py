import cv2
import numpy as np
import urllib.request
import os

# Image URL
IMAGE_URL = "https://github.com/AIBauchi/.github/raw/main/profile/image.png"

# Get directory of current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Output path
output_path = os.path.join(BASE_DIR, "grayscale_image.png")

# -----------------------------
# Load image from URL
# -----------------------------
resp = urllib.request.urlopen(IMAGE_URL)
image_data = np.asarray(bytearray(resp.read()), dtype=np.uint8)
image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

if image is None:
    print("❌ Error: Could not load image from URL")
    exit()

print("✅ Image loaded successfully from URL")

# -----------------------------
# Convert to Grayscale
# -----------------------------
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -----------------------------
# Save grayscale image
# -----------------------------
cv2.imwrite(output_path, gray_image)
print("✅ Grayscale image saved at:", output_path)

# -----------------------------
# Display results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
