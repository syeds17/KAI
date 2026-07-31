from Kai.api.llm.service import LLMService


llm = LLMService()

response = llm.chat(
    "Explain machine learning in one sentence."
)

print(response)