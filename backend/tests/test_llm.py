from Kai.api.llm.client import GeminiClient

client = GeminiClient()

print(client.generate("Say hello in one sentence."))