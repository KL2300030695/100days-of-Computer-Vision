import cv2
from datetime import datetime

# -----------------------------
# Open live camera
# -----------------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open camera")
    exit()

print("✅ Camera opened successfully")

# Username (fixed)
username = "Subhash Vadaparthi"

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame")
        break

    # Get current date
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Combine annotation text
    text = f"{username} | {current_date}"

    # Get frame dimensions
    height, width, _ = frame.shape

    # Position: lower-left corner
    x = 10
    y = height - 20

    # Draw text on frame
    cv2.putText(
        frame,
        text,
        (x, y),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),   # Yellow color
        2,
        cv2.LINE_AA
    )

    # Display the frame
    cv2.imshow("Day 6 - Real-time Annotation", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# -----------------------------
# Release resources
# -----------------------------
cap.release()
cv2.destroyAllWindows()
