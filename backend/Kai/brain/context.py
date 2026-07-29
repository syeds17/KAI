class Context:

    def __init__(self):
        self.history = []

    def add(self, user, assistant):
        self.history.append(
            {
                "user": user,
                "assistant": assistant
            }
        )