import re


class SlotExtractor:

    def extract(self, slot, text):

        if slot == "name":
            return self.extract_name(text)

        if slot == "extension":
            return self.extract_extension(text)

        if slot == "folder":
            return self.extract_folder(text)

        if slot == "number":
            return self.extract_number(text)

        return None


    def clean(self, text):

        text = text.lower()

        phrases = [
            "call it",
            "name it",
            "named",
            "name",
            "call",
            "create",
            "new",
            "folder",
            "file",
            "inside",
            "into",
            "in",
            "please"
        ]

        for phrase in phrases:
            text = text.replace(phrase, "")

        text = re.sub(r"\s+", " ", text)

        return text.strip()


    def extract_name(self, text):

        text = self.clean(text)
        
        if not text:
            return None

        return text


    def extract_extension(self, text):

        extensions = [
            ".py",
            ".txt",
            ".json",
            ".csv",
            ".md",
            ".html",
            ".css",
            ".js"
        ]

        for ext in extensions:

            if ext in text:
                return ext

        return None


    def extract_folder(self, text):

        match = re.search(r"(inside|into|in)\s+(.+)", text)

        if match:
            return match.group(2).strip()

        return None


    def extract_number(self, text):

        match = re.search(r"\d+", text)

        if match:
            return int(match.group())

        return None