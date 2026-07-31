import random

from .intent import IntentDetector
from .responses import RESPONSES
from memory.manager import MemoryManager

class CommandProcessor:

    def __init__(self):
        self.intent = IntentDetector()
        self.memory = MemoryManager()

    def process(self, command: str) -> str:

        intent = self.intent.detect(command)

        if intent == "remember":

            memory = command.replace("remember", "", 1).strip()

            if not memory:
                return "What would you like me to remember, Chief?"

            if self.memory.remember(memory):
                return "I'll remember that, Chief."
            
            return "You already told me that, Chief."

        if intent == "recall":

            memories = self.memory.recall()

            if not memories:
                return "I don't remember anything yet, Chief."

            lines = ["Here's what I remember, Chief:\n"]

            for idx, (_, text) in enumerate(memories, start=1):
                lines.append(f"  {idx}. {text}")

            return "\n".join(lines)

        return random.choice(RESPONSES[intent])