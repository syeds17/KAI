from .command import Command
from .actions import ACTIONS


class CommandParser:

    def parse(self, text: str) -> Command:

        words = text.lower().strip().split()

        if not words:
            return Command("unknown", "", text)

        action = words[0]

        if action not in ACTIONS:
            action = "unknown"

        target = " ".join(words[1:])

        return Command(
            action=action,
            target=target,
            raw=text
        )