from Kai.memory.manager import MemoryManager


memory = MemoryManager()

memory.save_conversation(
    "Hello KAI",
    "Hello Chief!"
)

memory.save_conversation(
    "Explain AI",
    "Artificial Intelligence is..."
)

print(memory.recent_conversations())
