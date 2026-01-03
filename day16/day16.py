import cv2
import os

# -----------------------------
# Load Haar Cascade safely
# -----------------------------
BASE_DIR = os.path.dirname(__file__)
cascade_path = os.path.join(
    BASE_DIR, "..", "cascades", "haarcascade_frontalface_default.xml"
)

print("Cascade path:", cascade_path)
print("Exists:", os.path.exists(cascade_path))

face_cascade = cv2.CascadeClassifier(cascade_path)

if face_cascade.empty():
    print("❌ Error: Failed to load Haar Cascade")
    exit()

print("✅ Haar Cascade loaded successfully")

# -----------------------------
# Open Live Camera
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open camera")
    exit()

print("✅ Camera opened successfully")

# -----------------------------
# Live Face Detection Loop
# -----------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale (required)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

    # Display result
    cv2.imshow("Day 16 - Live Face Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Cleanup
# -----------------------------
cap.release()
cv2.destroyAllWindows()
