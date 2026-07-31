from command.parser import CommandParser
from .dispatcher import Dispatcher
from .normalizer import Normalizer


class Router:

    def __init__(self):
        self.parser = CommandParser()
        self.dispatcher = Dispatcher()
        self.normalizer = Normalizer()

    def route(self, text: str):

        text = self.normalizer.normalize(text)
        command = self.parser.parse(text)

        return self.dispatcher.dispatch(command)