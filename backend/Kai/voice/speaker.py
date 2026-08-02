import pyttsx3

from .config import (
    VOICE_RATE,
    VOICE_VOLUME,
    VOICE_ID
)


class Speaker:

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", VOICE_RATE)
        self.engine.setProperty("volume", VOICE_VOLUME)

        if VOICE_ID:
            self.engine.setProperty("voice", VOICE_ID)

    def say(self, text: str):

        print(f"KAI 🔊 {text}")

        self.engine.say(text)
        self.engine.runAndWait()