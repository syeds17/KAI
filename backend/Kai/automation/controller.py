from .executor import Executor
from .registry import APPLICATIONS, WEBSITES, FOLDERS


class AutomationController:

    def __init__(self):
        self.executor = Executor()

    def _find_match(self, registry, target):

        target = target.lower().strip()

        for item in registry.values():

            if target in item["aliases"]:
                return item

        return None

    def open(self, target: str):

        app = self._find_match(APPLICATIONS, target)

        if app:
            self.executor.execute_application(app["command"])
            return f"Opening {app['name']}, Chief."

        website = self._find_match(WEBSITES, target)

        if website:
            self.executor.execute_website(website["url"])
            return f"Opening {website['name']}, Chief."

        folder = self._find_match(FOLDERS, target)

        if folder:
            self.executor.execute_folder(folder["path"])
            return f"Opening {folder['name']}, Chief."

        return f"I couldn't find '{target}', Chief."
    
    def close(self, target: str):

        for registry in [APPLICATIONS, WEBSITES]:

            item = self._find_match(registry, target)

            if item:

                self.executor.close_process(
                    item["close_process"]
               )

                return f"Closing {item['name']}, Chief."

        return f"I couldn't find '{target}', Chief."