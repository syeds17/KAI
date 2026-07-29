from .processor import CommandProcessor


class Router:

    def __init__(self):
        self.processor = CommandProcessor()

    def route(self, command: str):

        return self.processor.process(command)