import sqlite3
from pathlib import Path


class MemoryStorage:
    """
    Handles all database operations for KAI's memory.
    """

    def __init__(self):
        self.db_path = Path(__file__).parent / "kai_memory.db"
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

        self.create_table()

    def create_table(self):
        """Create the memories table if it doesn't exist."""

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        """)

        self.connection.commit()

    def save_memory(self, content: str):
        """Save a memory to the database."""

        self.cursor.execute(
            "INSERT INTO memories (content) VALUES (?)",
            (content,)
        )

        self.connection.commit()

    def get_memories(self):
        """Return all stored memories."""

        self.cursor.execute(
            "SELECT id, content FROM memories"
        )

        return self.cursor.fetchall()

    def delete_memory(self, memory_id: int):
        """Delete a memory by ID."""

        self.cursor.execute(
            "DELETE FROM memories WHERE id = ?",
            (memory_id,)
        )

        self.connection.commit()