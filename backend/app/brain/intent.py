class IntentDetector:

    def detect(self, command: str) -> str:

        command = command.lower().strip()

        if command in ["hello", "hi", "hey"]:
            return "greeting"

        if command in ["who are you", "what is your name"]:
            return "identity"

        if command in ["how are you"]:
            return "status"

        return "unknown"