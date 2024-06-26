import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic

cap = cv2.VideoCapture('C:/Users/ADMIN/AppData/Local/Programs/Python/Python310/face/dance - done/Pushpa2.mp4')
background = cv2.VideoCapture('C:/Users/ADMIN/AppData/Local/Programs/Python/Python310/face/dance - done/background.mp4')

with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:

    while cap.isOpened():
        _, image = cap.read()
        _, backgroundimage = background.read()

        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result = holistic.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(
            backgroundimage,
            result.face_landmarks,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles.get_default_face_mesh_contours_style())

        mp_drawing.draw_landmarks(
            backgroundimage,
            result.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        cv2.imshow("Holistic figure", cv2.flip(backgroundimage, 1))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cap.release()
