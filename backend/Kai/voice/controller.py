from .listener import Listener
from .speaker import Speaker
from .wakeword import WakeWordDetector


class VoiceController:

    def __init__(self):

        self.listener = Listener()
        self.speaker = Speaker()
        self.wakeword = WakeWordDetector()

    def listen(self):

        return self.listener.listen()

    def speak(self, text: str):

        self.speaker.say(text)

    def wait_for_wake_word(self):

        text = self.listen()

        if self.wakeword.detected(text):

            self.speak("Yes, Chief.")

            return True

        return False