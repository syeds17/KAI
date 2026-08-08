import re

from .command import Command


class FileCommandParser:

    def parse(self, text: str):

        original = text
        text = text.strip()

        lower = text.lower()

        # ---------------- WRITE ----------------

        if lower.startswith("write "):

            match = re.match(
                r"write\s+(.+?)\s+(?:in|into|to)\s+(.+)",
                text,
                re.IGNORECASE
            )

            if match:

                return Command(
                    action="write",
                    target=match.group(2).strip(),
                    content=match.group(1).strip(),
                    raw=original
                )

            content = text[6:].strip()

            for ending in (" in", " into", " to"):
                if content.endswith(ending):
                    content = content[:-len(ending)].strip()
                    
            return Command(
                action="write",
                target="",
                content=content,
                raw=original
            )

        # ---------------- APPEND ----------------

        if lower.startswith("append "):

            match = re.match(
                r"append\s+(.+?)\s+(?:in|into|to)\s+(.+)",
                text,
                re.IGNORECASE
            )

            if match:

                return Command(
                    action="append",
                    target=match.group(2).strip(),
                    content=match.group(1).strip(),
                    raw=original
                )
                
            content = text[7:].strip()

            for ending in (" in", " into", " to"):
                if content.endswith(ending):
                    content = content[:-len(ending)].strip()   

            return Command(
                action="append",
                target="",
                content=content,
                raw=original
            )

        # ---------------- CLEAR ----------------

        if lower.startswith("clear "):

            return Command(
                action="clear",
                target=text[6:].strip(),
                raw=original
            )

        # ---------------- REPLACE ----------------

        if lower.startswith("replace "):

            match = re.match(
                r"replace\s+(.+?)\s+with\s+(.+?)\s+in\s+(.+)",
                text,
                re.IGNORECASE
            )

            if match:

                old = match.group(1).strip()
                new = match.group(2).strip()
                target = match.group(3).strip()

                return Command(
                    action="replace",
                    target=f"{target}|{old}|{new}",
                    raw=original
                )

        return Command(
            action="unknown",
            raw=original
        )