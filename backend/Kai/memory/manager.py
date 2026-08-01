from .storage import MemoryStorage


class MemoryManager:
    """
    High-level interface for KAI's memory system.
    """

    def __init__(self):
        self.storage = MemoryStorage()

    def remember(self, content: str) -> bool:

        if self.storage.memory_exists(content):
            return False

        self.storage.save_memory(content)
        return True

    def recall(self):
        return self.storage.get_memories()

    def forget(self, memory_id: int):
        self.storage.delete_memory(memory_id)
    
    def save_conversation(self, user_message: str, assistant_message: str):
        self.storage.save_conversation(user_message, assistant_message)

    def recent_conversations(self, limit: int = 10):
        return self.storage.get_recent_conversations(limit)