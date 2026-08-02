import time


class ConversationManager:
    """
    Handles KAI's conversation state.
    """

    def __init__(self, timeout=25):

        self.timeout = timeout
        self.active = False
        self.last_activity = 0

    def start(self):

        self.active = True
        self.last_activity = time.time()

    def stop(self):

        self.active = False

    def refresh(self):

        self.last_activity = time.time()

    def is_active(self):

        if not self.active:
            return False, False

        if time.time() - self.last_activity > self.timeout:

            self.active = False

            return False, True

        return True, False