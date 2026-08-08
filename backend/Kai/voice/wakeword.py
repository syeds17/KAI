import re


class WakeWordDetector:
    """
    Detects KAI's wake word and extracts any command
    spoken immediately after it.
    """

    def __init__(self):

        self.wake_patterns = [
            r"\bokay\s+kai+\b",
            r"\bhey\s+kai+\b",
            r"\bhi\s+kai+\b",
            r"\bkai+\b",
            r"\bkay+\b",
        ]

    def extract_command(self, text: str):

        if not text:
            return None

        text = text.lower().strip()

        for pattern in self.wake_patterns:

            match = re.search(pattern, text)

            if match:

                command = text[match.end():].strip()

                return command

        return None

    def detected(self, text: str):

        return self.extract_command(text) is not None