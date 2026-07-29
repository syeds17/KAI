from command.parser import CommandParser
from .dispatcher import Dispatcher


class Router:

    def __init__(self):
        self.parser = CommandParser()
        self.dispatcher = Dispatcher()

    def route(self, text: str):

        command = self.parser.parse(text)

        return self.dispatcher.dispatch(command)