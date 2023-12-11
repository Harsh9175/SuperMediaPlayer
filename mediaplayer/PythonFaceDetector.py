# import cv2
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
#
# class FaceRecognitionApp(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.camera = cv2.VideoCapture(0)  # Open the camera
#
#         self.image_label = QLabel(self)
#         self.image_label.setAlignment(Qt.AlignCenter)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.image_label)
#         self.setLayout(layout)
#
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)  # Update every 30 milliseconds
#
#     def update_frame(self):
#         ret, frame = self.camera.read()
#         if not ret:
#             return
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = image.shape
#         bytes_per_line = ch * w
#         q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         self.image_label.setPixmap(QPixmap.fromImage(q_image))
#
#     def closeEvent(self, event):
#         self.camera.release()
#         self.timer.stop()
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     window = FaceRecognitionApp()
#     window.setWindowTitle("Face Recognition")
#     window.show()
#     sys.exit(app.exec_())
#

# Working Perfectly..........
# import cv2
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
#
# class FaceRecognitionApp(QWidget):
#     def __init__(self, video_player):
#         super().__init__()
#
#         self.video_player = video_player
#
#         self.camera = cv2.VideoCapture(0)  # Open the camera
#
#         self.image_label = QLabel(self)
#         self.image_label.setAlignment(Qt.AlignCenter)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.image_label)
#         self.setLayout(layout)
#
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)  # Update every 30 milliseconds
#
#     def update_frame(self):
#         ret, frame = self.camera.read()
#         if not ret:
#             return
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = image.shape
#         bytes_per_line = ch * w
#         q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         self.image_label.setPixmap(QPixmap.fromImage(q_image))
#
#         if len(faces) > 0:
#             self.video_player.set_playing(True)  # Play the video if face detected
#         else:
#             self.video_player.set_playing(False)  # Pause the video if no face detected
#
#     def closeEvent(self, event):
#         self.camera.release()
#         self.timer.stop()
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = None  # Create a placeholder for the VideoPlayer instance
#     window = FaceRecognitionApp(player)
#     window.setWindowTitle("Face Recognition")
#     window.show()
#     sys.exit(app.exec_())

# Working for hand and face recognitions part 2
# import cv2
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
#
# class FaceRecognitionApp(QWidget):
#     def __init__(self, video_player):
#         super().__init__()
#
#         self.video_player = video_player
#
#         self.camera = cv2.VideoCapture(0)  # Open the camera
#
#         self.image_label = QLabel(self)
#         self.image_label.setAlignment(Qt.AlignCenter)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.image_label)
#         self.setLayout(layout)
#
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)  # Update every 30 milliseconds
#
#     def update_frame(self):
#         ret, frame = self.camera.read()
#         if not ret:
#             return
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = image.shape
#         bytes_per_line = ch * w
#         q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         self.image_label.setPixmap(QPixmap.fromImage(q_image))
#
#         if len(faces) > 0:
#             self.video_player.set_playing(True)  # Play the video if face detected
#         else:
#             self.video_player.set_playing(False)  # Pause the video if no face detected
#
#     def closeEvent(self, event):
#         self.camera.release()
#         self.timer.stop()
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = None  # Create a placeholder for the VideoPlayer instance
#     window = FaceRecognitionApp(player)
#     window.setWindowTitle("Face Recognition")
#     window.show()
#     sys.exit(app.exec_())

# Fist, Palm, Face Working
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget

class FaceRecognitionApp(QWidget):
    def __init__(self, video_player):
        super().__init__()

        self.video_player = video_player

        self.camera = cv2.VideoCapture(0)  # Open the camera

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # Update every 30 milliseconds

    def update_frame(self):
        ret, frame = self.camera.read()
        if not ret:
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = image.shape
        bytes_per_line = ch * w
        q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_image))

        if len(faces) > 0:
            self.video_player.set_playing(True)  # Play the video if face detected
        else:
            self.video_player.set_playing(False)  # Pause the video if no face detected

    def closeEvent(self, event):
        self.camera.release()
        self.timer.stop()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player = None  # Create a placeholder for the VideoPlayer instance
    window = FaceRecognitionApp(player)
    window.setWindowTitle("Face Recognition")
    window.show()
    sys.exit(app.exec_())



# Trying 30aug
# import cv2
# from PyQt5.QtCore import Qt, QTimer
# from PyQt5.QtGui import QImage, QPixmap
# from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
#
# class FaceRecognitionApp(QWidget):
#     def __init__(self, video_player):
#         super().__init__()
#
#         self.video_player = video_player
#         self.palm_detected = False  # Add a flag for palm detection
#
#         self.camera = cv2.VideoCapture(0)  # Open the camera
#
#         self.image_label = QLabel(self)
#         self.image_label.setAlignment(Qt.AlignCenter)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.image_label)
#         self.setLayout(layout)
#
#         self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#
#         self.timer = QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(30)  # Update every 30 milliseconds
#
#     def update_frame(self):
#         ret, frame = self.camera.read()
#         if not ret:
#             return
#
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
#         image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         h, w, ch = image.shape
#         bytes_per_line = ch * w
#         q_image = QImage(image.data, w, h, bytes_per_line, QImage.Format_RGB888)
#         self.image_label.setPixmap(QPixmap.fromImage(q_image))
#
#         if len(faces) > 0:
#             self.video_player.set_playing(True)  # Play the video if face detected
#             self.palm_detected = False  # Reset palm detection flag
#         else:
#             self.video_player.set_playing(False)  # Pause the video if no face detected
#
#     def is_palm_detected(self):
#         return self.palm_detected  # Return palm detection status
#
#     def closeEvent(self, event):
#         self.camera.release()
#         self.timer.stop()
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = None  # Create a placeholder for the VideoPlayer instance
#     window = FaceRecognitionApp(player)
#     window.setWindowTitle("Face Recognition")
#     window.show()
#     sys.exit(app.exec_())
