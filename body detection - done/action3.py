import cv2
import mediapipe as mp
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)  # Suppress deprecation warnings

# Initialize MediaPipe pose model
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Video source from the webcam
cap = cv2.VideoCapture(0)

# Set the size of the output window
cv2.namedWindow('Pose Detection', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Pose Detection', 800, 800)  # You can adjust the size as needed

def calculate_angle(landmark1, landmark2, landmark3):
    vector1 = np.array([landmark1.x - landmark2.x, landmark1.y - landmark2.y])
    vector2 = np.array([landmark3.x - landmark2.x, landmark3.y - landmark2.y])
    unit_vector1 = vector1 / np.linalg.norm(vector1)
    unit_vector2 = vector2 / np.linalg.norm(vector2)
    dot_product = np.dot(unit_vector1, unit_vector2)
    angle = np.arccos(dot_product) / np.pi * 180
    return angle

def detect_action(landmarks, prev_landmarks):
    # Check if landmarks list is empty
    if not landmarks:
        return "Unknown"
    
    # Extract necessary landmarks
    hip_left = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]
    knee_left = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    ankle_left = landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value]
    hip_knee_angle_left = calculate_angle(hip_left, knee_left, ankle_left)
    if hip_knee_angle_left > 160:
        return "Standing"
    elif hip_knee_angle_left < 100:
        return "Sitting"
    # Add more conditions here for walking, running, etc.
    return "Unknown"

def detect_dance(landmarks):
    # Check if landmarks list is empty
    if not landmarks:
        return "Unknown Dance Move"
    
    # Check if both hands are above the shoulders
    shoulder_left = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    shoulder_right = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
    hand_left = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]
    hand_right = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]
    
    # Define threshold for hand elevation
    threshold = 0.1  # Adjust as needed
    
    # Check if both hands are above the shoulders
    if hand_left.y < shoulder_left.y - threshold and hand_right.y < shoulder_right.y - threshold:
        return "Dancing"
    else:
        return "Unknown Dance Move"

def detect_jumping(landmarks):
    # Check if landmarks list is empty
    if not landmarks:
        return "Unknown Jumping Move"
    
    # Check if both knees are bent
    knee_left = landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value]
    knee_right = landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value]
    
    # Define threshold for knee bending
    threshold = 0.1  # Adjust as needed
    
    # Check if both knees are bent
    if knee_left.y < knee_right.y - threshold:
        return "Jumping"
    else:
        return "Unknown Jumping Move"

# Additional action detection functions (walking, running, fighting) can be implemented similarly

colors = [(0, 255, 0), (0, 0, 255), (255, 0, 0)]  # Colors for different persons

persons = []  # List to store information about each person detected

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        
        if results.pose_landmarks is not None:
            if len(persons) < len(results.pose_landmarks.landmark):
                persons = [{'landmarks': []} for _ in range(len(results.pose_landmarks.landmark))]
            
            for idx, person in enumerate(persons):
                if idx < len(results.pose_landmarks.landmark):
                    landmark = results.pose_landmarks.landmark[idx]
                    person['landmarks'].append(landmark)
                    
                    landmarks = person['landmarks']
                    action = detect_action(landmarks, None)  # Pass None or previous landmarks if tracking over frames
                    dance_move = detect_dance(landmarks)
                    color = colors[idx % len(colors)]  # Cycle through colors for each person
                    mp_drawing.draw_landmarks(frame, landmarks, mp_pose.POSE_CONNECTIONS,
                                              mp_drawing.DrawingSpec(color=color, thickness=2, circle_radius=2),
                                              mp_drawing.DrawingSpec(color=color, thickness=2))
                    cv2.putText(frame, action, (50, 100 + idx * 150), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
                    cv2.putText(frame, dance_move, (50, 150 + idx * 150), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2, cv2.LINE_AA)
        
        cv2.imshow('Pose Detection', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release the capture and destroy any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()
