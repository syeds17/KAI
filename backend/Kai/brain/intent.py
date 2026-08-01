class IntentDetector:

    def __init__(self):

        self.rules = {
            "greeting": [
                "hello",
                "hi",
                "hey"
            ],

            "identity": [
                "who are you",
                "what is your name"
            ],

            "status": [
                "how are you"
            ],

            "recall": [
                "what do you remember",
                "show memories",
                "show memory",
                "list memories"
            ],

            "open": [
                "open",
                "launch",
                "start"
            ],

            "close": [
                "close",
                "exit",
                "quit",
                "terminate",
                "kill"
            ],
            
            "search": [
                "find",
                "search",
                "locate"
            ],

            "create_folder": [
                "create folder",
                "make folder",
                "new folder"
            ],

            "open_file": [
                "open file",
                "open folder",
                "open"
            ]
        }


    def detect(self, command: str) -> str:

        print("DETECTING:", command)
        
        command = command.lower().strip()

        if command.startswith("remember "):
            return "remember"

        for intent, keywords in self.rules.items():

            for keyword in keywords:

                if command.startswith(keyword):
                    return intent

        return "unknown"