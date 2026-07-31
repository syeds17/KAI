import re


class Normalizer:
    """
    Converts natural language into KAI's internal command format.
    """

    def normalize(self, text: str) -> str:
        text = text.lower().strip()

        replacements = {
            r"\bplease\b": "",
            r"\bcould you\b": "",
            r"\bcan you\b": "",
            r"\bwould you\b": "",
            r"\bkindly\b": "",
            r"\blaunch\b": "open",
            r"\bstart\b": "open",
            r"\brun\b": "open",
        }

        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text)

        # Remove extra spaces
        text = " ".join(text.split())

        return text