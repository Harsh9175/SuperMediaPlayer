# import speech_recognition as sr
#
# # Initialize the recognizer
# recognizer = sr.Recognizer()
#
# # Use the default microphone as the audio source
# with sr.Microphone() as source:
#     print("Listening...")
#
#     # Adjust for ambient noise before capturing audio
#     recognizer.adjust_for_ambient_noise(source)
#
#     # Capture audio from the microphone
#     audio = recognizer.listen(source)
#
#     try:
#         # Perform speech recognition
#         text = recognizer.recognize_google(audio)
#         print("You said:", text)
#     except sr.UnknownValueError:
#         print("Sorry, I could not understand what you said.")
#     except sr.RequestError as e:
#         print("Sorry, there was an error connecting to the Google API. Error:", e)
#


import speech_recognition as sr
from PyQt5.QtCore import QThread, pyqtSignal

class SpeechRecognitionThread(QThread):
    speech_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.recognizer = sr.Recognizer()

    def run(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            while True:
                audio = self.recognizer.listen(source)
                try:
                    text = self.recognizer.recognize_google(audio)
                    print("Player Paused")
                    self.speech_signal.emit(text)
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    print("Sorry, there was an error connecting to the Google API. Error:", e)
