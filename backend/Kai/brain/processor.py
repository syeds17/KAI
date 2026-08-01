import random

from .intent import IntentDetector
from .responses import RESPONSES
from memory.manager import MemoryManager
from api.llm.service import LLMService

class CommandProcessor:

    def __init__(self):
        self.intent = IntentDetector()
        self.memory = MemoryManager()
        self.llm = LLMService()

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

        if intent == "unknown":

            conversations = self.memory.recent_conversations()

            context = ""

            if conversations:

                context = "Recent Conversation:\n\n"

                for user, assistant in reversed(conversations):
                    context += f"User: {user}\n"
                    context += f"KAI: {assistant}\n\n"

            response = self.llm.chat(command, context)

            self.memory.save_conversation(command, response)

            return response

        response = random.choice(RESPONSES[intent])

        self.memory.save_conversation(command, response)

        return response