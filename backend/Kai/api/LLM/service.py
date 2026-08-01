from .client import GeminiClient
from .prompts import SYSTEM_PROMPT


class LLMService:

    def __init__(self):
        self.client = GeminiClient()

    def chat(self, user_input: str, context: str = "") -> str:

        prompt = f"""
    {SYSTEM_PROMPT}

    Conversation History:
    {context}

    Current User:
    {user_input}

    Respond as KAI:
    """

        return self.client.generate(prompt)