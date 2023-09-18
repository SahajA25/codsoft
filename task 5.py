import cv2
import face_recognition

# Initialize video capture (0 represents the default webcam)
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read a frame from the camera.")
        break

    # Detect face locations and encodings using face_recognition
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Iterate through detected faces
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Display the name "Sahaj" for all detected faces
        name = "Sahaj"

        # Draw a rectangle around the face and display the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name , (left + 6, bottom - 6), font, 0.5, (255, 0, 0), 2)

    # Display the frame with rectangles and names
    cv2.imshow('Face Detection and Recognition', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# Release the camera and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()