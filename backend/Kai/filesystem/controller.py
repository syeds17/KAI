from pathlib import Path

from .manager import FileManager


class FilesystemController:
    """
    Controls KAI's file system actions.
    """

    def __init__(self):

        self.manager = FileManager()
        self.last_results = []

    def search(self, target: str):

        results = self.manager.search(target)
        self.last_results = results

        if not results:
            return f"I couldn't find '{target}', Chief."

        response = "I found these, Chief:\n\n"

        for index, item in enumerate(results[:5], start=1):
            response += f"{index}. {Path(item).name}\n"

        return response

    def open(self, target: str):

        # User selected a previous search result
        if target.isdigit():

            index = int(target) - 1

            if 0 <= index < len(self.last_results):

                path = self.last_results[index]

                if self.manager.open(path):
                    return f"Opening '{Path(path).name}', Chief."

                return "I couldn't open that item, Chief."

            return "That search result doesn't exist, Chief."

        # User entered a normal path
        if self.manager.open(target):
            return f"Opening '{Path(target).name}', Chief."

        return "I couldn't open that, Chief."

    def create_folder(self, folder_name: str):

        documents = Path.home() / "Documents"
        folder_path = documents / folder_name

        if self.manager.create_folder(str(folder_path)):
            return f"Folder '{folder_name}' created in Documents, Chief."

        return f"Folder '{folder_name}' already exists in Documents, Chief."
    
    def create_file(self, file_name: str):

        documents = Path.home() / "Documents"
        file_path = documents / file_name

        if self.manager.create_file(str(file_path)):
            return f"File '{file_name}' created in Documents, Chief."

        return f"File '{file_name}' already exists in Documents, Chief."
    
    def rename(self, target: str):

        if "|" not in target:
            return "Please specify both file names, Chief."

        old_name, new_name = target.split("|", 1)

        documents = Path.home() / "Documents"

        old_path = documents / old_name
        new_path = documents / new_name

        if self.manager.rename(str(old_path), str(new_path)):
            return f"Renamed '{old_name}' to '{new_name}', Chief."

        return f"I couldn't find '{old_name}', Chief."
    
    def copy(self, target: str):

        if "|" not in target:
            return "Please specify both file names, Chief."

        source, destination = target.split("|", 1)

        documents = Path.home() / "Documents"
 
        source_path = documents / source
        destination_path = documents / destination

        if self.manager.copy(str(source_path), str(destination_path)):
            return f"Copied '{source}' to '{destination}', Chief."

        return f"I couldn't find '{source}', Chief."
    
    def move(self, target: str):

        if "|" not in target:
            return "Please specify both file names, Chief."

        source, destination = target.split("|", 1)

        documents = Path.home() / "Documents"

        source_path = documents / source
        destination_path = documents / destination

        if self.manager.move(str(source_path), str(destination_path)):
            return f"Moved '{source}' to '{destination}', Chief."

        return f"I couldn't find '{source}', Chief."
    
    def delete(self, target: str):

        documents = Path.home() / "Documents"
        target_path = documents / target

        if self.manager.delete(str(target_path)):
            return f"Deleted '{target}', Chief."

        return f"I couldn't find '{target}', Chief."
    
    def read(self, target: str):

        documents = Path.home() / "Documents"
        file_path = documents / target

        content = self.manager.read(str(file_path))

        if content is None:
            return f"I couldn't read '{target}', Chief."

        if content == "Unsupported file type.":
            return f"'{target}' is not a supported file type yet, Chief."

        if not content.strip():
            return f"'{target}' is empty, Chief."

        MAX_CHARS = 3000

        if len(content) > MAX_CHARS:
            content = content[:MAX_CHARS] + "\n\n...(Content truncated)"

        return f"Contents of '{target}':\n\n{content}"