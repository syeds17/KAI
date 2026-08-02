import re


class ParameterExtractor:

    def extract_name(self, text: str):

        text = text.lower().strip()

        # Remove common conversational prefixes
        prefixes = [
            "call it",
            "name it",
            "name",
            "called",
            "named",
            "it is",
            "it's",
            "its",
            "make it",
        ]

        for prefix in prefixes:
            if text.startswith(prefix):
                text = text[len(prefix):].strip()

        # Remove articles
        words_to_remove = {
            "a", "an", "the"
        }

        words = [w for w in text.split() if w not in words_to_remove]

        text = " ".join(words)

        # Convert spoken extensions
        replacements = {
            " dot py": ".py",
            " dot txt": ".txt",
            " dot pdf": ".pdf",
            " dot docx": ".docx",
            " dot csv": ".csv",
            " dot json": ".json",
        }

        for old, new in replacements.items():
            text = text.replace(old, new)

        # Remove duplicate spaces
        text = re.sub(r"\s+", " ", text)

        return text.strip()