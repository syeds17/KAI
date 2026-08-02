import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        print("🎤 Calibrating microphone...")

        with self.microphone as source:

            self.recognizer.adjust_for_ambient_noise(source, duration=2)

        print("✅ Microphone ready, Chief.")

    def listen(self):

        with self.microphone as source:

            print("🎤 Listening...")

            audio = self.recognizer.listen(source)

        try:

            command = self.recognizer.recognize_google(audio).lower()
            command = command.replace("guy", "kai")
            command = command.replace("sky", "kai")
            command = command.replace("ky", "kai")
            command = command.replace("ki", "kai")

            print(f"Chief: {command}")

            return command.lower()

        except sr.UnknownValueError:

            return None

        except sr.RequestError:

            return None