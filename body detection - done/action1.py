import cv2
import mediapipe as mp

# Initialize the MediaPipe pose model
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose_detection = mp_pose.Pose()

# Set the input video source
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video source
    ret, frame = cap.read()

    # Flip the frame horizontally for a more natural view
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB format
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Run the MediaPipe pose model
    results = pose_detection.process(frame_rgb)

    # Draw the pose landmarks on the frame
    if results.pose_landmarks is not None:
        mp_drawing.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
            connection_drawing_spec=mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)
        )

    # Display the output frame
    cv2.imshow('Output', frame)

    # Check for user input
    c = cv2.waitKey(1)

    # Break the loop if the user presses the 'q' key
    if c == ord('q'):
        break

# Release the video source and destroy all windows
cap.release()
cv2.destroyAllWindows()
