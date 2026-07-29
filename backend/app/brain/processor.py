import random

from .intent import IntentDetector
from .responses import RESPONSES


class CommandProcessor:

    def __init__(self):
        self.intent = IntentDetector()

    def process(self, command: str) -> str:

        intent = self.intent.detect(command)

        return random.choice(RESPONSES[intent])