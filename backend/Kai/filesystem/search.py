from pathlib import Path


class FileSearch:
    """
    Handles searching files and folders.
    """

    def __init__(self):
        self.home = Path.home()


    def search(self, name: str):

        results = []

        name = name.lower()

        for path in self.home.rglob("*"):

            try:
                if name in path.name.lower():
                    results.append(str(path))

            except PermissionError:
                continue

        return results