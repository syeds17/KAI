class IntentDetector:

    def detect(self, command: str) -> str:

        command = command.lower().strip()

        if command in ["hello", "hi", "hey"]:
            return "greeting"

        if command in ["who are you", "what is your name"]:
            return "identity"

        if command in ["how are you"]:
            return "status"
        if command.startswith("remember "):
            return "remember"

        if command in [
            "what do you remember",
            "show memories",
            "show memory",
            "list memories"
        ]:
            return "recall"

        return "unknown"