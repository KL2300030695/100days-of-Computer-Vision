import cv2

# -----------------------------
# Open live camera (0 = default webcam)
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not access the camera")
    exit()

print("✅ Camera opened successfully")

while True:
    ret, frame = cap.read()

    if not ret:
        print("❌ Failed to grab frame")
        break

    # Get frame dimensions
    height, width, _ = frame.shape

    # Center of the frame
    center_x = width // 2
    center_y = height // 2

    # Draw a circle at the center
    cv2.circle(
        frame,                      # image
        (center_x, center_y),        # center
        60,                          # radius
        (0, 255, 0),                 # color (green)
        3                            # thickness
    )

    # Display the frame
    cv2.imshow("Live Camera - Circle Drawing", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Release resources
# -----------------------------
cap.release()
cv2.destroyAllWindows()
