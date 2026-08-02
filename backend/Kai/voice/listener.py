import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()

    def listen(self):

        with sr.Microphone() as source:

            print("🎤 Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:

            command = self.recognizer.recognize_google(audio)

            print(f"Chief: {command}")

            return command.lower()

        except sr.UnknownValueError:

            return None

        except sr.RequestError:

            return None