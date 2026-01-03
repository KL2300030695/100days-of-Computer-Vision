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
# Preprocessing
# -----------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

_, binary = cv2.threshold(
    blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# -----------------------------
# Find Contours
# -----------------------------
contours, _ = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

output = image.copy()

# -----------------------------
# Shape Detection
# -----------------------------
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < 500:
        continue  # ignore noise

    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)

    shape = "Unknown"

    if len(approx) == 3:
        shape = "Triangle"

    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        shape = "Square" if 0.95 <= aspect_ratio <= 1.05 else "Rectangle"

    else:
        shape = "Circle"

    # Draw contour
    cv2.drawContours(output, [cnt], -1, (0, 255, 0), 2)

    # Label shape
    x, y = approx[0][0]
    cv2.putText(
        output,
        shape,
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255, 0, 0),
        2
    )

# -----------------------------
# Display Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Contours & Shape Detection", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
