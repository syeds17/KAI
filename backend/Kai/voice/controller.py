from .listener import Listener
from .speaker import Speaker


class VoiceController:

    def __init__(self):

        self.listener = Listener()
        self.speaker = Speaker()

    def listen(self):

        return self.listener.listen()

    def speak(self, text: str):

        self.speaker.say(text)