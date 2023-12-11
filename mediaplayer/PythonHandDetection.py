# import cv2
#
# # Load the Haar cascade classifier for hand detection
# hand_cascade = cv2.CascadeClassifier('path_to_hand_cascade.xml')
#
# # Initialize video capture
# cap = cv2.VideoCapture(0)  # Use 0 for the default webcam
#
# while True:
#     # Read a frame from the video capture
#     ret, frame = cap.read()
#
#     # Convert to grayscale for detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Detect hands
#     hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Draw rectangles around detected hands
#     for (x, y, w, h) in hands:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Hand Detection', frame)
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the capture
# cap.release()
# cv2.destroyAllWindows()


# Working for hand recognitions
# import cv2
#
# hand_cascade = cv2.CascadeClassifier('haarcascade_hand.xml')
#
# # Initialize video capture
# cap = cv2.VideoCapture(0)  # Use 0 for the default webcam
#
# while True:
#     # Read a frame from the video capture
#     ret, frame = cap.read()
#
#     # Convert to grayscale for detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Detect hands
#     hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Draw rectangles around detected hands
#     for (x, y, w, h) in hands:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Hand Detection', frame)
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the capture
# cap.release()
# cv2.destroyAllWindows()

# Fist, Palm, Face Working
import cv2

hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_palm.xml')

cap = cv2.VideoCapture(0)  # Use 0 for the default webcam

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert to grayscale for detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hands
    hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected hands
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('Hand Detection', frame)

    # Check for fist and palm and control video player
    if len(hands) > 0:
        if self.is_fist(hands[0]):
            player.set_playing(False)  # Pause the video if fist detected
        else:
            player.set_playing(True)  # Play the video if palm detected

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv2.destroyAllWindows()



# 30AugHome - Trying to implement PRIORITY
# import cv2
#
# hand_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_palm.xml')
#
# cap = cv2.VideoCapture(0)  # Use 0 for the default webcam
#
# while True:
#     # Read a frame from the video capture
#     ret, frame = cap.read()
#
#     # Convert to grayscale for detection
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     # Detect hands
#     hands = hand_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#     # Draw rectangles around detected hands
#     for (x, y, w, h) in hands:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
#     # Display the frame
#     cv2.imshow('Hand Detection', frame)
#
#     # Check for fist and palm and control video player
#     if len(hands) > 0:
#         if self.is_fist(hands[0]):
#             self.palm_detected = False  # Reset palm detection flag
#             player.set_playing(False)  # Pause the video if fist detected
#         else:
#             self.palm_detected = True  # Set palm detection flag
#             if not self.is_face_detected():
#                 player.set_playing(True)  # Play the video if palm detected and no face
#
#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # Release the capture
# cap.release()
# cv2.destroyAllWindows()
