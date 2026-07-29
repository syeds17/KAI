from command.parser import CommandParser
from automation.controller import AutomationController
from .processor import CommandProcessor


class Router:

    def __init__(self):
        self.parser = CommandParser()
        self.processor = CommandProcessor()
        self.automation = AutomationController()

    def route(self, text: str):

        command = self.parser.parse(text)

        if command.action == "open":
            return self.automation.open_application(command.target)

        return self.processor.process(text)