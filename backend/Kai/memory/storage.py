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

        self.create_tables()

    def create_tables(self):
        """Create all database tables."""

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
            )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_message TEXT NOT NULL,
            assistant_message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
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
    def memory_exists(self, content: str) -> bool:
        """Check whether a memory already exists."""

        self.cursor.execute(
            "SELECT 1 FROM memories WHERE LOWER(content) = LOWER(?)",
            (content,)
        )

        return self.cursor.fetchone() is not None

    def delete_memory(self, memory_id: int):
        """Delete a memory by ID."""

        self.cursor.execute(
            "DELETE FROM memories WHERE id = ?",
            (memory_id,)
        )

        self.connection.commit()
    
    def save_conversation(
        self,
            user_message: str,
            assistant_message: str
        ):
        """Save one conversation exchange."""

        self.cursor.execute(
        """
        INSERT INTO conversations
        (user_message, assistant_message)
        VALUES (?, ?)
        """,
        (user_message, assistant_message)
        )

        self.connection.commit()


    def get_recent_conversations(
        self,
        limit: int = 10
        ):
        """Return recent conversations."""

        self.cursor.execute(
        """
        SELECT
            user_message,
            assistant_message
        FROM conversations
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
        )

        return self.cursor.fetchall()