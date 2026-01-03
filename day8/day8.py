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

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Reduce noise using Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)

    # Display results
    cv2.imshow("Live Camera", frame)
    cv2.imshow("Canny Edge Detection", edges)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Release resources
# -----------------------------
cap.release()
cv2.destroyAllWindows()
