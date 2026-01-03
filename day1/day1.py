import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture a single frame
ret, frame = cap.read()

if ret:
    # Save the image to the local directory
    cv2.imwrite('captured_image.jpg', frame)
    print("Image captured and saved as 'captured_image.jpg'")
else:
    print("Error: Could not capture image.")

# Release the camera
cap.release()