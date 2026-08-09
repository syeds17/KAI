import speech_recognition as sr


class Listener:

    def __init__(self):

        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        # Better defaults
        self.recognizer.pause_threshold = 0.8
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.5
        self.recognizer.dynamic_energy_threshold = True

        print("🎤 Calibrating microphone...")

        with self.microphone as source:

            self.recognizer.adjust_for_ambient_noise(source, duration=2)

        print("✅ Microphone ready, Chief.")

    def listen(self, timeout=5, phrase_time_limit=10):

        attempts = 2

        for _ in range(attempts):

            with self.microphone as source:

                if _ == 0:
                    print("🎤 Listening...")

                try:

                    audio = self.recognizer.listen(
                        source,
                        timeout=timeout,
                        phrase_time_limit=phrase_time_limit 
                    )

                except sr.WaitTimeoutError:
                    continue

            try:

                command = self.recognizer.recognize_google(audio).lower()

                command = self._normalize(command)

                print(f"Chief: {command}")

                return command

            except sr.UnknownValueError:

                # Didn't understand, try again silently
                continue

            except sr.RequestError:

                print("⚠ Speech recognition service unavailable.")

                return None

        return None

    def _normalize(self, command: str):
        
        command = command.lower().strip()

        replacements = {
           "kaii": "kai",
           "kahi": "kai",
           "guy": "kai",
           "sky": "kai",
           "ky": "kai",
           "ki": "kai",
           "kay": "kai",
           "bhai": "kai",
           "ka": "kai",
        }

        for wrong, correct in replacements.items():
            command = command.replace(wrong, correct)

        return command.strip()