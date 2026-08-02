from command.parser import CommandParser
from .dispatcher import Dispatcher
from .normalizer import Normalizer
from .preprocessor import Preprocessor
from .parser.splitter import CommandSplitter
from .conversation.manager import ConversationManager



class Router:

    def __init__(self):

        self.parser = CommandParser()
        self.dispatcher = Dispatcher()
        self.normalizer = Normalizer()
        self.preprocessor = Preprocessor()
        self.splitter = CommandSplitter()
        self.conversation = ConversationManager()

    def route(self, text: str):

        
        text = self.preprocessor.clean(text)


        text = self.normalizer.normalize(text)

        print(f"PROCESSED: {text}")


        commands = self.splitter.plan(text)

        responses = []

        for item in commands:

            command = self.parser.parse(item)

            command, message = self.conversation.handle(command)

            if message is not None:
                responses.append(message)
                continue
            
            if command is None:
                continue

            response = self.dispatcher.dispatch(command)

            responses.append(response)

        return "\n".join(responses)