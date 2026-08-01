import os


class Explorer:
    """
    Handles opening files and folders.
    """

    def open(self, path: str):

        if not os.path.exists(path):
            return False

        os.startfile(path)

        return True