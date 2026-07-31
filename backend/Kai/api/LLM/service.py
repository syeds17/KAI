from .client import GeminiClient
from .prompts import SYSTEM_PROMPT


class LLMService:

    def __init__(self):
        self.client = GeminiClient()

    def chat(self, user_input: str) -> str:

        prompt = f"""
{SYSTEM_PROMPT}

User:
{user_input}

KAI:
"""

        return self.client.generate(prompt)