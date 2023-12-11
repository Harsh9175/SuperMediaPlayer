# from PyQt5.QtCore import QDir, Qt, QUrl
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
#         QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget)
# from PyQt5.QtWidgets import QMainWindow,QWidget, QPushButton, QAction
# from PyQt5.QtGui import QIcon
# import sys
#
# class VideoPlayer(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQt5 Video Player")
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#
#         videoWidget = QVideoWidget()
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.error = QLabel()
#         self.error.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
#
#         openButton = QPushButton("Open Video")
#         openButton.setToolTip("Open Video File")
#         openButton.setStatusTip("Open Video File")
#         openButton.setFixedHeight(24)
#         openButton.clicked.connect(self.openFile)
#
#
#         # Create a widget for window contents
#         wid = QWidget(self)
#         self.setCentralWidget(wid)
#
#         # Create layouts to place inside widget
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.error)
#         layout.addWidget(openButton)
#
#         # Set widget to contain window contents
#         wid.setLayout(layout)
#
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#
#     def openFile(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
#                 QDir.homePath())
#
#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                     QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)
#
#     def exitCall(self):
#         sys.exit(app.exec_())
#
#     def play(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#         else:
#             self.mediaPlayer.play()
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.error.setText("Error: " + self.mediaPlayer.errorString())
#
#
# app = QApplication(sys.argv)
# videoplayer = VideoPlayer()
# videoplayer.resize(640, 480)
# videoplayer.show()
# sys.exit(app.exec_())

# Parth 2nd one
# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtCore import QDir, Qt, QUrl, QSize
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
#         QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar)
#
# class VideoPlayer(QWidget):
#
#     def __init__(self, parent=None):
#         super(VideoPlayer, self).__init__(parent)
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#
#         btnSize = QSize(16, 16)
#         videoWidget = QVideoWidget()
#
#         openButton = QPushButton("Open Video")
#         openButton.setToolTip("Open Video File")
#         openButton.setStatusTip("Open Video File")
#         openButton.setFixedHeight(24)
#         openButton.setIconSize(btnSize)
#         openButton.setFont(QFont("Noto Sans", 8))
#         openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
#         openButton.clicked.connect(self.abrir)
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setFixedHeight(24)
#         self.playButton.setIconSize(btnSize)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.statusBar = QStatusBar()
#         self.statusBar.setFont(QFont("Noto Sans", 7))
#         self.statusBar.setFixedHeight(14)
#
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(openButton)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.statusBar)
#
#         self.setLayout(layout)
#
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#         self.statusBar.showMessage("Ready")
#
#     def abrir(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Selecciona los mediose",
#                 ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")
#
#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                     QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)
#             self.statusBar.showMessage(fileName)
#             self.play()
#
#     def play(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#         else:
#             self.mediaPlayer.play()
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                     self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = VideoPlayer()
#     player.setWindowTitle("Player")
#     player.resize(600, 400)
#     player.show()
#     sys.exit(app.exec_())

# Face Recognition
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


# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtCore import Qt, QUrl, QSize
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (
#     QApplication, QFileDialog, QHBoxLayout, QLabel,
#     QPushButton, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar
# )
#
# from PythonFaceDetector import FaceRecognitionApp
#
# class VideoPlayerWithFaceRecognition(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.face_recognition_app = FaceRecognitionApp()  # Initialize the face recognition app
#
#         btnSize = QSize(16, 16)
#         videoWidget = QVideoWidget()
#
#         openButton = QPushButton("Open Video")
#         openButton.setToolTip("Open Video File")
#         openButton.setStatusTip("Open Video File")
#         openButton.setFixedHeight(24)
#         openButton.setIconSize(btnSize)
#         openButton.setFont(QFont("Noto Sans", 8))
#         openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
#         openButton.clicked.connect(self.abrir)
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setFixedHeight(24)
#         self.playButton.setIconSize(btnSize)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.statusBar = QStatusBar()
#         self.statusBar.setFont(QFont("Noto Sans", 7))
#         self.statusBar.setFixedHeight(14)
#
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(openButton)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.statusBar)
#
#         self.setLayout(layout)
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#         self.statusBar.showMessage("Ready")
#
#     def abrir(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Select media",
#             ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")
#
#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                 QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)
#             self.statusBar.showMessage(fileName)
#             self.play()
#
#     def play(self):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.mediaPlayer.pause()
#         else:
#             self.mediaPlayer.play()
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
#
#     def closeEvent(self, event):
#         self.face_recognition_app.camera.release()  # Release the camera
#         self.face_recognition_app.timer.stop()  # Stop the timer
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = VideoPlayerWithFaceRecognition()
#     player.setWindowTitle("Player with Face Recognition")
#     player.resize(600, 500)
#     player.show()
#     sys.exit(app.exec_())

# Working Perfectly for face detection
# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtCore import Qt, QUrl, QSize
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (
#     QApplication, QFileDialog, QHBoxLayout, QLabel,
#     QPushButton, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar
# )
#
# from PythonFaceDetector import FaceRecognitionApp
#
# class VideoPlayerWithFaceRecognition(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.face_recognition_app = FaceRecognitionApp(self)  # Initialize the face recognition app
#         self.is_playing = False  # Initialize the face recognition app
#
#         btnSize = QSize(16, 16)
#         videoWidget = QVideoWidget()
#
#         openButton = QPushButton("Open Video")
#         openButton.setToolTip("Open Video File")
#         openButton.setStatusTip("Open Video File")
#         openButton.setFixedHeight(24)
#         openButton.setIconSize(btnSize)
#         openButton.setFont(QFont("Noto Sans", 8))
#         openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
#         openButton.clicked.connect(self.abrir)
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setFixedHeight(24)
#         self.playButton.setIconSize(btnSize)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.statusBar = QStatusBar()
#         self.statusBar.setFont(QFont("Noto Sans", 7))
#         self.statusBar.setFixedHeight(14)
#
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(openButton)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.statusBar)
#
#         self.setLayout(layout)
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#         self.statusBar.showMessage("Ready")
#
#     def abrir(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Select media",
#             ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")
#
#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                 QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)
#             self.statusBar.showMessage(fileName)
#             self.play()
#
#     def set_playing(self, state):
#         if state:
#             self.mediaPlayer.play()
#             self.is_playing = True
#         else:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#
#     def play(self):
#         if self.is_playing:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#         else:
#             self.mediaPlayer.play()
#             self.is_playing = True
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
#
#     def closeEvent(self, event):
#         self.face_recognition_app.camera.release()  # Release the camera
#         self.face_recognition_app.timer.stop()  # Stop the timer
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = VideoPlayerWithFaceRecognition()
#     player.setWindowTitle("Player with Face Recognition")
#     player.resize(600, 500)
#     player.show()
#     sys.exit(app.exec_())
#


# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtCore import Qt, QUrl, QSize
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (
#     QApplication, QFileDialog, QHBoxLayout, QLabel,
#     QPushButton, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar
# )
#
# from PythonFaceDetector import FaceRecognitionApp
#
# class VideoPlayerWithFaceRecognition(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.face_recognition_app = FaceRecognitionApp(self)  # Initialize the face recognition app
#         self.is_playing = False
#
#         btnSize = QSize(16, 16)
#         videoWidget = QVideoWidget()
#
#         openButton = QPushButton("Open Video")
#         openButton.setToolTip("Open Video File")
#         openButton.setStatusTip("Open Video File")
#         openButton.setFixedHeight(24)
#         openButton.setIconSize(btnSize)
#         openButton.setFont(QFont("Noto Sans", 8))
#         openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
#         openButton.clicked.connect(self.abrir)
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setFixedHeight(24)
#         self.playButton.setIconSize(btnSize)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.statusBar = QStatusBar()
#         self.statusBar.setFont(QFont("Noto Sans", 7))
#         self.statusBar.setFixedHeight(14)
#
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(openButton)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.statusBar)
#
#         self.setLayout(layout)
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#         self.statusBar.showMessage("Ready")
#
#     def abrir(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Select media",
#             ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")
#
#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                 QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)
#             self.statusBar.showMessage(fileName)
#             self.play()
#
#     def set_playing(self, state):
#         if state:
#             self.mediaPlayer.play()
#             self.is_playing = True
#         else:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#
#     def play(self):
#         if self.is_playing:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#         else:
#             self.mediaPlayer.play()
#             self.is_playing = True
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
#
#     def closeEvent(self, event):
#         self.face_recognition_app.camera.release()  # Release the camera
#         self.face_recognition_app.timer.stop()  # Stop the timer
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = VideoPlayerWithFaceRecognition()
#     player.setWindowTitle("Player with Face Recognition")
#     player.resize(600, 500)
#     player.show()
#     sys.exit(app.exec_())

# Fist, Palm, Face Working --- MAIN
# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtCore import Qt, QUrl, QSize
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (
#     QApplication, QFileDialog, QHBoxLayout, QLabel,
#     QPushButton, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar
# )
#
# from PythonFaceDetector import FaceRecognitionApp
#
# class VideoPlayerWithFaceRecognition(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.face_recognition_app = FaceRecognitionApp(self)  # Initialize the face recognition app
#         self.is_playing = False  # Initialize the face recognition app
#
#         btnSize = QSize(16, 16)
#         videoWidget = QVideoWidget()
#
#         openButton = QPushButton("Open Video")
#         openButton.setToolTip("Open Video File")
#         openButton.setStatusTip("Open Video File")
#         openButton.setFixedHeight(24)
#         openButton.setIconSize(btnSize)
#         openButton.setFont(QFont("Noto Sans", 8))
#         openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
#         openButton.clicked.connect(self.abrir)
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setFixedHeight(24)
#         self.playButton.setIconSize(btnSize)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.statusBar = QStatusBar()
#         self.statusBar.setFont(QFont("Noto Sans", 7))
#         self.statusBar.setFixedHeight(14)
#
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(openButton)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.statusBar)
#
#         self.setLayout(layout)
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#         self.statusBar.showMessage("Ready")
#
#     def abrir(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Select media",
#             ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")
#
#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                 QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)
#             self.statusBar.showMessage(fileName)
#             self.play()
#
#     def set_playing(self, state):
#         if state:
#             self.mediaPlayer.play()
#             self.is_playing = True
#         else:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#
#     def play(self):
#         if self.is_playing:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#         else:
#             self.mediaPlayer.play()
#             self.is_playing = True
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
#
#     def closeEvent(self, event):
#         self.face_recognition_app.camera.release()  # Release the camera
#         self.face_recognition_app.timer.stop()  # Stop the timer
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = VideoPlayerWithFaceRecognition()
#     player.setWindowTitle("Player with Face Recognition")
#     player.resize(600, 500)
#     player.show()
#     sys.exit(app.exec_())
#






# SpeechRecognition Module --- Issues
# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtCore import Qt, QUrl, QSize
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (
#     QApplication, QFileDialog, QHBoxLayout, QLabel,
#     QPushButton, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar
# )
#
# from PythonFaceDetector import FaceRecognitionApp
# import speech_recognition as sr
#
#
# class VideoPlayerWithFaceRecognition(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.face_recognition_app = FaceRecognitionApp(self)  # Initialize the face recognition app
#         self.is_playing = False  # Initialize the face recognition app
#
#         btnSize = QSize(16, 16)
#         videoWidget = QVideoWidget()
#
#         openButton = QPushButton("Open Video")
#         openButton.setToolTip("Open Video File")
#         openButton.setStatusTip("Open Video File")
#         openButton.setFixedHeight(24)
#         openButton.setIconSize(btnSize)
#         openButton.setFont(QFont("Noto Sans", 8))
#         openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
#         openButton.clicked.connect(self.abrir)
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setFixedHeight(24)
#         self.playButton.setIconSize(btnSize)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.statusBar = QStatusBar()
#         self.statusBar.setFont(QFont("Noto Sans", 7))
#         self.statusBar.setFixedHeight(14)
#
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(openButton)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.statusBar)
#
#         self.setLayout(layout)
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#         self.statusBar.showMessage("Ready")
#
#     def abrir(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Select media",
#             ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")
#
#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                 QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)
#             self.statusBar.showMessage(fileName)
#             self.play()
#
#     def set_playing(self, state):
#         if state:
#             self.mediaPlayer.play()
#             self.is_playing = True
#         else:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#
#     def play(self):
#         if self.is_playing:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#         else:
#             self.mediaPlayer.play()
#             self.is_playing = True
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
#
#     def closeEvent(self, event):
#         self.face_recognition_app.camera.release()  # Release the camera
#         self.face_recognition_app.timer.stop()  # Stop the timer
#
#
# class SpeechRecognitionApp(QWidget):
#     def __init__(self, video_player):
#         super().__init__()
#
#         self.video_player = video_player
#
#         self.recognizer = sr.Recognizer()
#
#         self.microphone_button = QPushButton("Start Listening")
#         self.microphone_button.clicked.connect(self.start_listening)
#
#         layout = QVBoxLayout()
#         layout.addWidget(self.microphone_button)
#         self.setLayout(layout)
#
#     def start_listening(self):
#         with sr.Microphone() as source:
#             print("Listening for voice commands...")
#
#             self.recognizer.adjust_for_ambient_noise(source)
#
#             audio = self.recognizer.listen(source)
#
#             try:
#                 text = self.recognizer.recognize_google(audio)
#                 print("You said:", text)
#
#                 if "PLAY" in text.upper():
#                     self.video_player.set_playing(True)
#                 elif "STOP" in text.upper():
#                     self.video_player.set_playing(False)
#             except sr.UnknownValueError:
#                 print("Sorry, I could not understand the voice command.")
#             except sr.RequestError as e:
#                 print("Error connecting to the Google API:", e)
#
# # ... (same as before)
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = VideoPlayerWithFaceRecognition()
#     speech_app = SpeechRecognitionApp(player)
#
#     h_layout = QHBoxLayout()
#     h_layout.addWidget(player)
#     h_layout.addWidget(speech_app)
#
#     main_widget = QWidget()
#     main_widget.setLayout(h_layout)
#     main_widget.setWindowTitle("Player with Voice Recognition")
#     main_widget.resize(1000, 500)
#     main_widget.show()
#
#     sys.exit(app.exec_())




# 30AugHome - Trying to implement PRIORITY
# from PyQt5.QtGui import QIcon, QFont
# from PyQt5.QtCore import Qt, QUrl, QSize
# from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtWidgets import (
#     QApplication, QFileDialog, QHBoxLayout, QLabel,
#     QPushButton, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar
# )
#
# from PythonFaceDetector import FaceRecognitionApp
#
# class VideoPlayerWithFaceRecognition(QWidget):
#     def __init__(self):
#         super().__init__()
#
#         self.face_recognition_app = FaceRecognitionApp(self)  # Initialize the face recognition app
#         self.is_playing = False  # Initialize the face recognition app
#
#         btnSize = QSize(16, 16)
#         videoWidget = QVideoWidget()
#
#         openButton = QPushButton("Open Video")
#         openButton.setToolTip("Open Video File")
#         openButton.setStatusTip("Open Video File")
#         openButton.setFixedHeight(24)
#         openButton.setIconSize(btnSize)
#         openButton.setFont(QFont("Noto Sans", 8))
#         openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
#         openButton.clicked.connect(self.abrir)
#
#         self.playButton = QPushButton()
#         self.playButton.setEnabled(False)
#         self.playButton.setFixedHeight(24)
#         self.playButton.setIconSize(btnSize)
#         self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
#         self.playButton.clicked.connect(self.play)
#
#         self.positionSlider = QSlider(Qt.Horizontal)
#         self.positionSlider.setRange(0, 0)
#         self.positionSlider.sliderMoved.connect(self.setPosition)
#
#         self.statusBar = QStatusBar()
#         self.statusBar.setFont(QFont("Noto Sans", 7))
#         self.statusBar.setFixedHeight(14)
#
#         controlLayout = QHBoxLayout()
#         controlLayout.setContentsMargins(0, 0, 0, 0)
#         controlLayout.addWidget(openButton)
#         controlLayout.addWidget(self.playButton)
#         controlLayout.addWidget(self.positionSlider)
#
#         layout = QVBoxLayout()
#         layout.addWidget(videoWidget)
#         layout.addLayout(controlLayout)
#         layout.addWidget(self.statusBar)
#
#         self.setLayout(layout)
#
#         self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
#         self.mediaPlayer.setVideoOutput(videoWidget)
#         self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
#         self.mediaPlayer.positionChanged.connect(self.positionChanged)
#         self.mediaPlayer.durationChanged.connect(self.durationChanged)
#         self.mediaPlayer.error.connect(self.handleError)
#         self.statusBar.showMessage("Ready")
#
#     def abrir(self):
#         fileName, _ = QFileDialog.getOpenFileName(self, "Select media",
#             ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")
#
#         if fileName != '':
#             self.mediaPlayer.setMedia(
#                 QMediaContent(QUrl.fromLocalFile(fileName)))
#             self.playButton.setEnabled(True)
#             self.statusBar.showMessage(fileName)
#             self.play()
#
#     def set_playing(self, state):
#         if state:
#             if not self.face_recognition_app.is_palm_detected():
#                 self.mediaPlayer.play()  # Play the video if no palm
#                 self.is_playing = True
#             else:
#                 self.mediaPlayer.pause()  # Pause if palm detected
#                 self.is_playing = False
#         else:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#
#     def is_face_detected(self):
#         return self.face_recognition_app.is_face_detected()
#
#     def play(self):
#         if self.is_playing:
#             self.mediaPlayer.pause()
#             self.is_playing = False
#         else:
#             self.mediaPlayer.play()
#             self.is_playing = True
#
#     def mediaStateChanged(self, state):
#         if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPause))
#         else:
#             self.playButton.setIcon(
#                 self.style().standardIcon(QStyle.SP_MediaPlay))
#
#     def positionChanged(self, position):
#         self.positionSlider.setValue(position)
#
#     def durationChanged(self, duration):
#         self.positionSlider.setRange(0, duration)
#
#     def setPosition(self, position):
#         self.mediaPlayer.setPosition(position)
#
#     def handleError(self):
#         self.playButton.setEnabled(False)
#         self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())
#
#     def closeEvent(self, event):
#         self.face_recognition_app.camera.release()  # Release the camera
#         self.face_recognition_app.timer.stop()  # Stop the timer
#
# if __name__ == '__main__':
#     import sys
#     app = QApplication(sys.argv)
#     player = VideoPlayerWithFaceRecognition()
#     player.setWindowTitle("Player with Face and Hand Recognition")
#     player.resize(600, 500)
#     player.show()
#     sys.exit(app.exec_())


from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QUrl, QSize, QThread
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (
    QApplication, QFileDialog, QHBoxLayout, QLabel,
    QPushButton, QSlider, QStyle, QVBoxLayout, QWidget, QStatusBar
)

from PythonFaceDetector import FaceRecognitionApp
from SpeechRecognition import SpeechRecognitionThread

class VideoPlayerWithFaceRecognition(QWidget):
    def __init__(self):
        super().__init__()

        self.face_recognition_app = FaceRecognitionApp(self)  # Initialize the face recognition app
        self.is_playing = False  # Initialize the face recognition app

        btnSize = QSize(16, 16)
        videoWidget = QVideoWidget()

        openButton = QPushButton("Open Video")
        openButton.setToolTip("Open Video File")
        openButton.setStatusTip("Open Video File")
        openButton.setFixedHeight(24)
        openButton.setIconSize(btnSize)
        openButton.setFont(QFont("Noto Sans", 8))
        openButton.setIcon(QIcon.fromTheme("document-open", QIcon("D:/_Qt/img/open.png")))
        openButton.clicked.connect(self.abrir)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setFixedHeight(24)
        self.playButton.setIconSize(btnSize)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.statusBar = QStatusBar()
        self.statusBar.setFont(QFont("Noto Sans", 7))
        self.statusBar.setFixedHeight(14)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.statusBar)

        self.setLayout(layout)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)
        self.statusBar.showMessage("Ready")

        self.speech_thread = SpeechRecognitionThread()
        self.speech_thread.speech_signal.connect(self.handle_speech_command)
        self.speech_thread.start()

    def handle_speech_command(self, command):
        if command == "START":
            self.set_playing(True)
        elif command == "STOP":
            self.set_playing(False)
            # Explicitly pause the media player when "STOP" is detected
            self.mediaPlayer.pause()

    def abrir(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Select media",
                                                  ".", "Video Files (*.mp4 *.flv *.ts *.mts *.avi *.mkv)")

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)
            self.statusBar.showMessage(fileName)
            self.play()

    def set_playing(self, state):
        if state:
            self.mediaPlayer.play()
            self.is_playing = True
        else:
            self.mediaPlayer.pause()
            self.is_playing = False

    def play(self):
        if self.is_playing:
            self.mediaPlayer.pause()
            self.is_playing = False
        else:
            self.mediaPlayer.play()
            self.is_playing = True

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.statusBar.showMessage("Error: " + self.mediaPlayer.errorString())

    def closeEvent(self, event):
        self.face_recognition_app.camera.release()  # Release the camera
        self.face_recognition_app.timer.stop()  # Stop the timer

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player = VideoPlayerWithFaceRecognition()
    player.setWindowTitle("Super Media Player")
    player.resize(600, 500)
    player.show()
    sys.exit(app.exec_())
