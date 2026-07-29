import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_NAME = os.getenv("PROJECT_NAME", "KAI")
OWNER_NAME = os.getenv("OWNER_NAME", "Chief")
VERSION = os.getenv("VERSION", "0.2.0")