from pathlib import Path
import shutil

class FileOperations:
    """
    Handles file and folder creation operations.
    """

    def create_folder(self, path: str):

        folder = Path(path)
        print("Creating folder at:", folder.resolve())

        if folder.exists():
            return False

        folder.mkdir(parents=True)

        return True


    def create_file(self, path: str):

        file = Path(path)

        if file.exists():
            return False

        file.touch()

        return True


    def rename(self, old_path: str, new_path: str):

        old = Path(old_path)

        if not old.exists():
            return False

        old.rename(new_path)

        return True
    
    def copy(self, source_path: str, destination_path: str):

        source = Path(source_path)

        if not source.exists():
            return False

        shutil.copy2(source, destination_path)

        return True
    
    def move(self, source_path: str, destination_path: str):

        source = Path(source_path)

        if not source.exists():
            return False

        source.rename(destination_path)

        return True
    
    def delete(self, path: str):

        item = Path(path)

        if not item.exists():
            return False

        if item.is_file():
            item.unlink()

        else:
            shutil.rmtree(item)

        return True