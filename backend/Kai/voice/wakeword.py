class WakeWordDetector:
    """
    Detects KAI's wake word.
    """

    def __init__(self):

        self.wake_words = [
            "kai",
            "okay kai",
            "hey kai",
            "hi kai"
        ]

    def detected(self, text: str) -> bool:

        if not text:
            return False

        text = text.lower().strip()

        return any(word in text for word in self.wake_words)