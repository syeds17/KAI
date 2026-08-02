import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")
        self.model = os.getenv(
            "GEMINI_MODEL",
            "gemini-flash-latest"
        )

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found"
            )

        self.client = genai.Client(
            api_key=api_key
        )


    def generate(self, prompt: str) -> str:

        try:

            response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"[LLM ERROR] {e}")

            return (
                "I'm unable to access my AI services right now, Chief. "
                "Please try again later."
            )