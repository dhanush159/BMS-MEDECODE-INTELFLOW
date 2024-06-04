# import cv2
# import mediapipe as mp
# import numpy as np

# # Initialize MediaPipe Face Mesh
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)
# draw = mp.solutions.drawing_utils

# # OpenCV setup
# cap = cv2.VideoCapture(0)  # Use 0 for webcam

# # Exercise states
# exercise_states = {
#     'extend_tongue': False,
#     'up_down_motion': False,
#     'left_right_motion': False,
#     'circular_motion': False
# }

# def detect_tongue_motion(tongue_tip_landmark):
#     global exercise_states
    
#     # Example exercises
#     # Extend tongue (simple motion detection)
#     if tongue_tip_landmark.y > 0.5:
#         exercise_states['extend_tongue'] = True
#     else:
#         exercise_states['extend_tongue'] = False
    
#     # Up-down motion (detect vertical movement)
#     if tongue_tip_landmark.y < 0.3:
#         exercise_states['up_down_motion'] = True
#     else:
#         exercise_states['up_down_motion'] = False
    
#     # Left-right motion (detect horizontal movement)
#     if tongue_tip_landmark.x < 0.3 or tongue_tip_landmark.x > 0.7:
#         exercise_states['left_right_motion'] = True
#     else:
#         exercise_states['left_right_motion'] = False
    
#     # Circular motion (detect circular movement)
#     # For simplicity, check if the tongue is moving in a circular path
#     if len(previous_tongue_positions) >= 3:
#         p1, p2, p3 = previous_tongue_positions[-3:]
#         vec1 = np.array([p2.x - p1.x, p2.y - p1.y])
#         vec2 = np.array([p3.x - p2.x, p3.y - p2.y])
#         cross_product = np.cross(vec1, vec2)
#         if abs(cross_product) > 0.02:  # Adjust threshold as needed
#             exercise_states['circular_motion'] = True
#         else:
#             exercise_states['circular_motion'] = False
#     else:
#         exercise_states['circular_motion'] = False

# # Previous tongue positions for circular motion detection
# previous_tongue_positions = []

# while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#         print("Ignoring empty camera frame.")
#         continue

#     # Convert the image to RGB
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Process the image with MediaPipe Face Mesh
#     results = face_mesh.process(image_rgb)

#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:
#             draw.draw_landmarks(image, face_landmarks, mp_face_mesh.FACEMESH_TESSELATION,
#                                 landmark_drawing_spec=draw.DrawingSpec(color=(0, 255, 0), thickness=1, circle_radius=1))

#             # Get tongue tip landmark (index 6)
#             if len(face_landmarks.landmark) > 6:
#                 tongue_tip = face_landmarks.landmark[6]
                
#                 # Store previous tongue positions for circular motion detection
#                 previous_tongue_positions.append(tongue_tip)
#                 if len(previous_tongue_positions) > 10:  # Keep only last 10 positions
#                     previous_tongue_positions.pop(0)
                
#                 # Detect tongue motions
#                 detect_tongue_motion(tongue_tip)

#             # Display exercise status
#             exercise_status_str = ''
#             if exercise_states['extend_tongue']:
#                 exercise_status_str += 'Extend Tongue\n'
#             if exercise_states['up_down_motion']:
#                 exercise_status_str += 'Up-Down Motion\n'
#             if exercise_states['left_right_motion']:
#                 exercise_status_str += 'Left-Right Motion\n'
#             if exercise_states['circular_motion']:
#                 exercise_status_str += 'Circular Motion\n'

#             if exercise_status_str == '':
#                 exercise_status_str = 'Perform Tongue Exercises'

#             cv2.putText(image, exercise_status_str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

#     # Display the resulting frame
#     cv2.imshow('Tongue Exercise Tracker', image)

#     # Exit the loop if 'q' is pressed
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()


import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Face Mesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# OpenCV setup
cap = cv2.VideoCapture(0)  # Use 0 for webcam

# Exercise states and thresholds
exercise_states = {
    'extend_tongue': False,
    'up_down_motion': False,
    'left_right_motion': False,
    'circular_motion': False
}

def detect_tongue_motion(tongue_tip_landmark):
    global exercise_states
    
    # Example exercises
    # Extend tongue (simple motion detection)
    if tongue_tip_landmark.y > 0.5:
        exercise_states['extend_tongue'] = True
    else:
        exercise_states['extend_tongue'] = False
    
    # Up-down motion (detect vertical movement)
    if tongue_tip_landmark.y < 0.3:
        exercise_states['up_down_motion'] = True
    else:
        exercise_states['up_down_motion'] = False
    
    # Left-right motion (detect horizontal movement)
    if tongue_tip_landmark.x < 0.3 or tongue_tip_landmark.x > 0.7:
        exercise_states['left_right_motion'] = True
    else:
        exercise_states['left_right_motion'] = False
    
    # Circular motion (detect circular movement)
    # For simplicity, check if the tongue is moving in a circular path
    if len(previous_tongue_positions) >= 3:
        p1, p2, p3 = previous_tongue_positions[-3:]
        vec1 = np.array([p2.x - p1.x, p2.y - p1.y])
        vec2 = np.array([p3.x - p2.x, p3.y - p2.y])
        cross_product = np.cross(vec1, vec2)
        if abs(cross_product) > 0.02:  # Adjust threshold as needed
            exercise_states['circular_motion'] = True
        else:
            exercise_states['circular_motion'] = False
    else:
        exercise_states['circular_motion'] = False

# Previous tongue positions for circular motion detection
previous_tongue_positions = []

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Face Mesh
    results = face_mesh.process(image_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get tongue tip landmark (index 6)
            if len(face_landmarks.landmark) > 6:
                tongue_tip = face_landmarks.landmark[6]
                
                # Store previous tongue positions for circular motion detection
                previous_tongue_positions.append(tongue_tip)
                if len(previous_tongue_positions) > 10:  # Keep only last 10 positions
                    previous_tongue_positions.pop(0)
                
                # Detect tongue motions
                detect_tongue_motion(tongue_tip)

    # Display exercise status
    exercise_status_str = ''
    if exercise_states['extend_tongue']:
        exercise_status_str += 'Extend Tongue\n'
    if exercise_states['up_down_motion']:
        exercise_status_str += 'Up-Down Motion\n'
    if exercise_states['left_right_motion']:
        exercise_status_str += 'Left-Right Motion\n'
    if exercise_states['circular_motion']:
        exercise_status_str += 'Circular Motion\n'

    if exercise_status_str == '':
        exercise_status_str = 'Perform Tongue Exercises'

    cv2.putText(image, exercise_status_str, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Tongue Exercise Tracker', image)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

# import cv2
# import mediapipe as mp
# import numpy as np

# # Initialize MediaPipe Face Mesh
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # OpenCV setup
# cap = cv2.VideoCapture(0)  # Use 0 for webcam

# # Exercise states and thresholds
# exercise_states = {
#     'extend_tongue': False,
#     'up_down_motion': False,
#     'left_right_motion': False,
#     'circular_motion': False
# }

# # Exercise completion states
# exercise_completed = {
#     'extend_tongue': False,
#     'up_down_motion': False,
#     'left_right_motion': False,
#     'circular_motion': False
# }

# # Exercise messages
# exercise_messages = {
#     'extend_tongue': 'Extend Tongue Exercise Completed!',
#     'up_down_motion': 'Up-Down Motion Exercise Completed!',
#     'left_right_motion': 'Left-Right Motion Exercise Completed!',
#     'circular_motion': 'Circular Motion Exercise Completed!'
# }

# # Function to detect tongue movements based on lip landmarks
# def detect_tongue_movements(lip_landmarks):
#     global exercise_states
    
#     # Example exercises
    
#     # Extend tongue (simple motion detection)
#     # Check if the tongue is lower than the lower lip
#     lower_lip_y = lip_landmarks[11].y  # Lower lip landmark index
#     tongue_y = lip_landmarks[7].y  # Tongue landmark index
#     if tongue_y < lower_lip_y:
#         exercise_states['extend_tongue'] = True
#     else:
#         exercise_states['extend_tongue'] = False
    
#     # Up-down motion (detect vertical movement)
#     # Compare upper and lower lip landmarks
#     upper_lip_y = lip_landmarks[8].y
#     lower_lip_y = lip_landmarks[11].y
#     if upper_lip_y - lower_lip_y > 0.03:  # Adjust threshold as needed
#         exercise_states['up_down_motion'] = True
#     else:
#         exercise_states['up_down_motion'] = False
    
#     # Left-right motion (detect horizontal movement)
#     # Compare left and right lip landmarks
#     left_lip_x = lip_landmarks[12].x
#     right_lip_x = lip_landmarks[4].x
#     if right_lip_x - left_lip_x > 0.03:  # Adjust threshold as needed
#         exercise_states['left_right_motion'] = True
#     else:
#         exercise_states['left_right_motion'] = False
    
#     # Circular motion (detect circular movement)
#     # For simplicity, not implemented in this example

# # Previous lip positions for circular motion detection
# previous_lip_positions = []

# while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#         print("Ignoring empty camera frame.")
#         continue

#     # Convert the image to RGB
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Process the image with MediaPipe Face Mesh
#     results = face_mesh.process(image_rgb)

#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:
#             # Check if the required lip landmarks are detected
#             if len(face_landmarks.landmark) > 10:  # Check for lip landmarks
#                 lip_landmarks = face_landmarks.landmark

#                 # Detect tongue movements
#                 detect_tongue_movements(lip_landmarks)

#                 # Check exercise completion
#                 for exercise in exercise_states:
#                     if exercise_states[exercise] and not exercise_completed[exercise]:
#                         exercise_completed[exercise] = True
#                         print(exercise_messages[exercise])  # Print message when exercise is completed

#     # Display detected tongue movements
#     detected_movements = []
#     for exercise in exercise_states:
#         if exercise_states[exercise]:
#             detected_movements.append(exercise.replace('_', ' ').title())

#     movement_str = ', '.join(detected_movements) if detected_movements else 'No Tongue Movement Detected'
#     cv2.putText(image, f'Detected Tongue Movements: {movement_str}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2, cv2.LINE_AA)

#     # Display the resulting frame
#     cv2.imshow('Tongue Exercise Tracker', image)

#     # Reset exercise completion states if no exercises are detected
#     if not any(exercise_states.values()):
#         exercise_completed = {
#             'extend_tongue': False,
#             'up_down_motion': False,
#             'left_right_motion': False,
#             'circular_motion': False
#         }

#     # Exit the loop if 'q' is pressed
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()


# import cv2
# import mediapipe as mp
# import numpy as np

# # Initialize MediaPipe Face Mesh
# mp_face_mesh = mp.solutions.face_mesh
# face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, min_detection_confidence=0.5, min_tracking_confidence=0.5)

# # OpenCV setup
# cap = cv2.VideoCapture(0)  # Use 0 for webcam

# # Exercise states and thresholds
# exercise_states = {
#     'extend_tongue': False,
#     'up_down_motion': False,
#     'left_right_motion': False,
#     'circular_motion': False
# }

# # Exercise completion states
# exercise_completed = {
#     'extend_tongue': False,
#     'up_down_motion': False,
#     'left_right_motion': False,
#     'circular_motion': False
# }

# # Exercise messages
# exercise_messages = {
#     'extend_tongue': 'Extend Tongue Exercise Completed!',
#     'up_down_motion': 'Up-Down Motion Exercise Completed!',
#     'left_right_motion': 'Left-Right Motion Exercise Completed!',
#     'circular_motion': 'Circular Motion Exercise Completed!'
# }

# # Function to detect tongue movements based on lip landmarks
# def detect_tongue_movements(lip_landmarks):
#     global exercise_states
    
#     # Example exercises
    
#     # Extend tongue (simple motion detection)
#     # Check if the tongue is lower than the lower lip
#     lower_lip_y = lip_landmarks[6][1]  # Lower lip center landmark index
#     tongue_y = lip_landmarks[10][1]  # Tongue tip landmark index
#     if tongue_y < lower_lip_y:
#         exercise_states['extend_tongue'] = True
#     else:
#         exercise_states['extend_tongue'] = False
    
#     # Up-down motion (detect vertical movement)
#     # Compare upper and lower lip landmarks
#     upper_lip_y = lip_landmarks[8][1]
#     lower_lip_y = lip_landmarks[6][1]
#     if upper_lip_y - lower_lip_y > 0.03:  # Adjust threshold as needed
#         exercise_states['up_down_motion'] = True
#     else:
#         exercise_states['up_down_motion'] = False
    
#     # Left-right motion (detect horizontal movement)
#     # Compare left and right lip landmarks
#     left_lip_x = lip_landmarks[4][0]
#     right_lip_x = lip_landmarks[12][0]
#     if right_lip_x - left_lip_x > 0.03:  # Adjust threshold as needed
#         exercise_states['left_right_motion'] = True
#     else:
#         exercise_states['left_right_motion'] = False
    
#     # Circular motion (detect circular movement)
#     # For simplicity, not implemented in this example

# # Previous lip positions for circular motion detection
# previous_lip_positions = []

# while cap.isOpened():
#     success, image = cap.read()
#     if not success:
#         print("Ignoring empty camera frame.")
#         continue

#     # Convert the image to RGB
#     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#     # Process the image with MediaPipe Face Mesh
#     results = face_mesh.process(image_rgb)

#     # Draw the lip mesh if landmarks are detected
#     if results.multi_face_landmarks:
#         for face_landmarks in results.multi_face_landmarks:
#             # Draw the face landmarks (lip mesh)
#             for i, landmark in enumerate(face_landmarks.landmark):
#                 x = int(landmark.x * image.shape[1])
#                 y = int(landmark.y * image.shape[0])
#                 cv2.circle(image, (x, y), 1, (0, 255, 0), -1)  # Draw a green dot for each landmark

#             # Check if the required lip landmarks are detected
#             if len(face_landmarks.landmark) > 20:  # Ensure enough landmarks are detected
#                 # Extract specific lip landmarks
#                 lip_landmarks = [(lm.x, lm.y) for lm in face_landmarks.landmark[2:14]]

#                 # Detect tongue movements
#                 detect_tongue_movements(lip_landmarks)

#                 # Check exercise completion
#                 for exercise in exercise_states:
#                     if exercise_states[exercise] and not exercise_completed[exercise]:
#                         exercise_completed[exercise] = True
#                         print(exercise_messages[exercise])  # Print message when exercise is completed

#     # Display the resulting frame with lip landmarks and detected tongue movements
#     cv2.imshow('Lip Landmarks and Tongue Exercises', image)

#     # Reset exercise completion states if no exercises are detected
#     if not any(exercise_states.values()):
#         exercise_completed = {
#             'extend_tongue': False,
#             'up_down_motion': False,
#             'left_right_motion': False,
#             'circular_motion': False
#         }

#     # Exit the loop if 'q' is pressed
#     if cv2.waitKey(5) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()



