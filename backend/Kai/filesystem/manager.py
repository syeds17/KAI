from .search import FileSearch
from .explorer import Explorer
from .operations import FileOperations
from .readers import FileReader


class FileManager:
    """
    High-level interface for KAI's file system.
    """

    def __init__(self):

        self.searcher = FileSearch()
        self.explorer = Explorer()
        self.operations = FileOperations()
        self.reader = FileReader()


    def search(self, name: str):

        return self.searcher.search(name)


    def open(self, path: str):

        return self.explorer.open(path)


    def create_folder(self, path: str):

        return self.operations.create_folder(path)


    def create_file(self, path: str):

        return self.operations.create_file(path)


    def rename(self, old_path: str, new_path: str):

        return self.operations.rename(old_path, new_path)


    def copy(self, source: str, destination: str):

        return self.operations.copy(source, destination)


    def move(self, source: str, destination: str):

        return self.operations.move(source, destination)


    def delete(self, path: str):

        return self.operations.delete(path)


    def read(self, path: str):

        return self.reader.read(path)