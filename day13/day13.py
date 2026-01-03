import cv2

# -----------------------------
# Open live camera
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open camera")
    exit()

print("✅ Camera opened successfully")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame")
        break

    # -----------------------------
    # Convert to Grayscale
    # -----------------------------
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # -----------------------------
    # Reduce noise
    # -----------------------------
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # -----------------------------
    # Adaptive Thresholding
    # -----------------------------
    sketch = cv2.adaptiveThreshold(
        blurred,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # -----------------------------
    # Display Results
    # -----------------------------
    cv2.imshow("Original Live Feed", frame)
    cv2.imshow("Pencil Sketch Effect", sketch)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Release resources
# -----------------------------
cap.release()
cv2.destroyAllWindows()
