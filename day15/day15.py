import cv2
import numpy as np

# -----------------------------
# Global Variables
# -----------------------------
drawing = False
last_x, last_y = -1, -1

# -----------------------------
# Mouse Callback Function
# -----------------------------
def paint(event, x, y, flags, param):
    global drawing, last_x, last_y, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(canvas, (last_x, last_y), (x, y), (0, 0, 255), 5)
            last_x, last_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

# -----------------------------
# Open Camera
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open camera")
    exit()

print("✅ Camera opened successfully")

# Read one frame to get dimensions
ret, frame = cap.read()
if not ret:
    print("❌ Failed to read frame")
    exit()

# Create a blank canvas
canvas = np.zeros_like(frame)

# Create window and attach mouse callback
cv2.namedWindow("Paint Brush Camera")
cv2.setMouseCallback("Paint Brush Camera", paint)

# -----------------------------
# Main Loop
# -----------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Combine frame and canvas
    painted_frame = cv2.add(frame, canvas)

    cv2.imshow("Paint Brush Camera", painted_frame)

    key = cv2.waitKey(1) & 0xFF

    # Press 'c' to clear canvas
    if key == ord('c'):
        canvas = np.zeros_like(frame)

    # Press 'q' to quit
    if key == ord('q'):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()
