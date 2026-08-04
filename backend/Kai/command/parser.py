from .command import Command
from .actions import ACTIONS
from .file_parser import FileCommandParser


ACTION_ALIASES = {
    "find": "search",
    "search": "search",
    "locate": "search",
}


class CommandParser:

    def __init__(self):

        self.file_parser = FileCommandParser()

    def parse(self, text: str) -> Command:

        words = text.lower().strip().split()

        if not words:
            return Command("unknown", "", text)

        action = words[0]

        # Delegate file editing commands
        if action in (
            "write",
            "append",
            "replace",
            "clear",
        ):
            return self.file_parser.parse(text)

        # Handle multi-word commands
        if len(words) >= 2:

            if words[0] in ("create", "make"):

                if words[1] == "folder":
                    action = "create_folder"

                elif words[1] == "file":
                    action = "create_file"

        # Handle rename
        if words[0] == "rename":
            action = "rename"

        # Handle copy
        if words[0] == "copy":
            action = "copy"

        # Handle move
        if words[0] == "move":
            action = "move"

        # Handle delete
        if words[0] == "delete":
            action = "delete"

        # Handle aliases
        if action in ACTION_ALIASES:
            action = ACTION_ALIASES[action]

        # Validate action
        if action not in ACTIONS:
            action = "unknown"

        # Extract target
        if action in ("create_folder", "create_file"):

            target = " ".join(words[2:])

        elif action in ("rename", "copy", "move"):

            if "to" not in words:
                target = ""

            else:
                index = words.index("to")

                source = " ".join(words[1:index])
                destination = " ".join(words[index + 1:])

                target = f"{source}|{destination}"

        else:

            target = " ".join(words[1:])

        return Command(
            action=action,
            target=target,
            raw=text
        )