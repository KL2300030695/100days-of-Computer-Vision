import cv2
import os

# Get the directory where THIS script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct path to image
image_path = os.path.join(BASE_DIR, "..", "day1", "captured_image.jpg")

print("Image path:", image_path)
print("Exists:", os.path.exists(image_path))

image = cv2.imread(image_path)

if image is None:
    print("Error: Could not load image")
    exit()

# Resize image
resized_image = cv2.resize(image, (256, 256))

cv2.imshow("Resized Image", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
