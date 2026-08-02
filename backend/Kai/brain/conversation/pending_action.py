class PendingAction:

    def __init__(self):
        self.clear()

    def set(self, action: str, slots: dict):
        self.action = action
        self.slots = slots

    def clear(self):
        self.action = None
        self.slots = {}

    def active(self):
        return self.action is not None

    def fill(self, key, value):
        self.slots[key] = value

    def get(self, key):
        return self.slots.get(key)

    def missing(self):
        return [k for k, v in self.slots.items() if v is None]