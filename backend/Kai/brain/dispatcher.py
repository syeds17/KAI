from automation.controller import AutomationController
from filesystem.controller import FilesystemController
from .processor import CommandProcessor


class Dispatcher:

    def __init__(self):

        self.automation = AutomationController()
        self.filesystem = FilesystemController()
        self.processor = CommandProcessor()

    def dispatch(self, command):

        if command.action == "open":

            # First try automation (apps, websites, folders)
            response = self.automation.open(command.target)

            # If automation succeeds, return immediately
            if "couldn't find" not in response.lower():
                return response

            # Otherwise try filesystem
            return self.filesystem.open(command.target)

        if command.action == "close":
            return self.automation.close(command.target)

        if command.action == "search":
            return self.filesystem.search(command.target)

        if command.action == "create_folder":
            return self.filesystem.create_folder(command.target)

        if command.action == "open_file":
            return self.filesystem.open(command.target)
        
        if command.action == "create_file":
            return self.filesystem.create_file(command.target)
        
        if command.action == "rename":
            return self.filesystem.rename(command.target)
        
        if command.action == "copy":
            return self.filesystem.copy(command.target)
        
        if command.action == "move":
            return self.filesystem.move(command.target)
        
        if command.action == "delete":
            return self.filesystem.delete(command.target)
        
        if command.action == "read":
            return self.filesystem.read(command.target)

        return self.processor.process(command.raw)