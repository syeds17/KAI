from .executor import Executor
from .registry import APPLICATIONS


class AutomationController:

    def __init__(self):
        self.executor = Executor()

    def open_application(self, target: str):

        application = APPLICATIONS.get(target)

        if application is None:
            return f"I couldn't find '{target}', Chief."

        self.executor.execute(application)

        return f"Opening {target.title()}, Chief."