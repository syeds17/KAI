import re
import pyttsx3

from .config import (
    VOICE_RATE,
    VOICE_VOLUME,
    VOICE_ID
)


class Speaker:
    """
    Handles KAI's text-to-speech.
    """

    def __init__(self):

        self.engine = pyttsx3.init()

        self.engine.setProperty("rate", VOICE_RATE)
        self.engine.setProperty("volume", VOICE_VOLUME)

        if VOICE_ID:
            self.engine.setProperty("voice", VOICE_ID)

    def clean_text(self, text: str) -> str:
        """
        Remove emojis and unsupported symbols before speaking.
        """

        return re.sub(r"[^\w\s.,!?':-]", "", text)

    def say(self, text: str):

        print(f"KAI 🔊 {text}")

        spoken_text = self.clean_text(text)

        self.engine.say(spoken_text)
        self.engine.runAndWait()