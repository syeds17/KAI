from .storage import MemoryStorage


class MemoryManager:
    """
    High-level interface for KAI's memory system.
    """

    def __init__(self):
        self.storage = MemoryStorage()

    def remember(self, content: str):
        self.storage.save_memory(content)

    def recall(self):
        return self.storage.get_memories()

    def forget(self, memory_id: int):
        self.storage.delete_memory(memory_id)