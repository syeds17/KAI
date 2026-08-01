from automation.controller import AutomationController
from .processor import CommandProcessor


class Dispatcher:

    def __init__(self):
        self.automation = AutomationController()
        self.processor = CommandProcessor()

    def dispatch(self, command):

        if command.action == "open":
            return self.automation.open(command.target)
        
        if command.action == "close":
            return self.automation.close(command.target)
        
        return self.processor.process(command.raw)