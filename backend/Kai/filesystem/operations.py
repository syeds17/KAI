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
    
    def exists(self, path: str):

        return Path(path).exists()
    
    def write(self, path: str, content: str):

        file = Path(path)

        file.parent.mkdir(parents=True, exist_ok=True)
        
        file.touch(exist_ok=True)

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

        return True
    
    def append(self, path: str, content: str):

        file = Path(path)

        file.parent.mkdir(parents=True, exist_ok=True)

        with open(file, "a", encoding="utf-8") as f:
            f.write("\n" + content)

        return True
    
    def clear(self, path: str):

        file = Path(path)

        if not file.exists():
            return False

        file.write_text("", encoding="utf-8")

        return True
    
    def replace(self, path: str, old: str, new: str):

        file = Path(path)

        if not file.exists():
            return False

        content = file.read_text(encoding="utf-8")

        content = content.replace(old, new)

        file.write_text(content, encoding="utf-8")

        return True