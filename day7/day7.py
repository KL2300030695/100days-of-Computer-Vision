import cv2
import os
import numpy as np

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
# Preprocessing
# -----------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binary threshold (Otsu)
_, binary = cv2.threshold(
    gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Invert if background is white
binary = cv2.bitwise_not(binary)

# -----------------------------
# Find Contours (Blobs)
# -----------------------------
contours, _ = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

output = image.copy()

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 500:  # ignore noise
        continue

    hull = cv2.convexHull(cnt)
    hull_area = cv2.contourArea(hull)
    if hull_area == 0:
        continue

    convexity = area / hull_area

    # Draw contour
    cv2.drawContours(output, [cnt], -1, (0, 255, 0), 2)

    # Draw convex hull
    cv2.drawContours(output, [hull], -1, (0, 0, 255), 2)

    # Label convexity
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.putText(
        output,
        f"Convexity: {convexity:.2f}",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (255, 0, 0),
        1
    )

# -----------------------------
# Display Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Binary Image", binary)
cv2.imshow("Blob Convexity Analysis", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
