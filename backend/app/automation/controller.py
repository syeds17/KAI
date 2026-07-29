from .executor import Executor
from .registry import APPLICATIONS


class AutomationController:

    def __init__(self):
        self.executor = Executor()

    def open_application(self, target: str):

        target = target.lower().strip()

        for app in APPLICATIONS.values():

            if target in app["aliases"]:

                self.executor.execute(app["command"])

                return f"Opening {app['name']}, Chief."

        return f"I couldn't find '{target}', Chief."