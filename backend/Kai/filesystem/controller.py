from pathlib import Path

from .manager import FileManager

from brain.runtime_context import runtime_context


class FilesystemController:
    """
    Controls KAI's file system actions.
    """

    def __init__(self):

        self.manager = FileManager()
        self.last_results = []
        
    def _resolve_path(self, target: str) -> Path:

        path = Path(target)

        if path.is_absolute():
            return path

        if runtime_context.current_directory:
            return Path(runtime_context.current_directory) / target

        return Path.home() / "Documents" / target    
        

    def search(self, target: str):

        results = self.manager.search(target)
        self.last_results = results
        runtime_context.last_search = results

        if not results:
            return f"I couldn't find '{target}', Chief."

        response = "I found these, Chief:\n\n"

        for index, item in enumerate(results[:5], start=1):
            response += f"{index}. {Path(item).name}\n"

        return response

    def open(self, target: str):
        
        if target.lower() == "it":

            if runtime_context.last_file:

                target = runtime_context.last_file

            else:

                return "I don't know what 'it' refers to yet, Chief."

        # User selected a previous search result
        if target.isdigit():

            index = int(target) - 1

            if 0 <= index < len(self.last_results):

                path = self.last_results[index]
                path_obj = Path(path)

                if path_obj.is_dir():
                    runtime_context.last_folder = str(path_obj)
                    runtime_context.current_directory = str(path_obj)
                else:
                    runtime_context.last_file = str(path_obj)

                if self.manager.open(path):
                    return f"Opening '{Path(path).name}', Chief."

                return "I couldn't open that item, Chief."

            return "That search result doesn't exist, Chief."

        # User entered a normal path
        path = self._resolve_path(target)

        if self.manager.open(str(path)):
            path_obj = path

            if path_obj.is_dir():
                runtime_context.last_folder = str(path_obj)
                runtime_context.current_directory = str(path_obj)
            else:
                runtime_context.last_file = str(path_obj)

            return f"Opening '{path_obj.name}', Chief."

        return "I couldn't open that, Chief."

    def create_folder(self, folder_name: str):

        base = (
            Path(runtime_context.current_directory)
            if runtime_context.current_directory
            else Path.home() / "Documents"
        )

        folder_path = base / folder_name

        if self.manager.create_folder(str(folder_path)):

            runtime_context.last_folder = str(folder_path)

            return f"Folder '{folder_name}' created in '{base.name}', Chief."

        return f"Folder '{folder_name}' already exists in '{base.name}', Chief."
    
    def create_file(self, file_name: str):

        location = None

    # Handle contextual location: "cat there"
        if "|" in file_name:

            file_name, location = file_name.rsplit("|", 1)

            file_name = file_name.strip()
            location = location.strip().lower()

    # Decide where the file should be created
        if location == "there" and runtime_context.last_folder:

            base = Path(runtime_context.last_folder)

        elif runtime_context.current_directory:

            base = Path(runtime_context.current_directory)

        else:

            base = Path.home() / "Documents"

        file_path = base / file_name

        if self.manager.create_file(str(file_path)):

            runtime_context.last_file = str(file_path)

            return f"File '{file_name}' created in '{base.name}', Chief."

        return f"File '{file_name}' already exists in '{base.name}', Chief."
    
    def rename(self, target: str):

        if target.startswith("it|"):

            if runtime_context.last_file:

                target = runtime_context.last_file + "|" + target[3:]

            else:

                return "I don't know what 'it' refers to yet, Chief."
        
        
        if "|" not in target:
            return "Please specify both file names, Chief."

        old_name, new_name = target.split("|", 1)

        old_path = self._resolve_path(old_name)

        new_path = old_path.parent / new_name

        if self.manager.rename(str(old_path), str(new_path)):

            runtime_context.last_file = str(new_path)

            return f"Renamed '{old_path.name}' to '{new_name}', Chief."

        return f"I couldn't find '{old_name}', Chief."
    
    def copy(self, target: str):

        if target.startswith("it|"):

            if runtime_context.last_file:

                target = runtime_context.last_file + "|" + target[3:]

            else:

                return "I don't know what 'it' refers to yet, Chief."
        
        if "|" not in target:
            return "Please specify both file names, Chief."

        source, destination = target.split("|", 1)
 
        source_path = self._resolve_path(source)
        destination_path = self._resolve_path(destination)

        if self.manager.copy(str(source_path), str(destination_path)):
            
            return f"Copied '{source}' to '{destination}', Chief."

        return f"I couldn't find '{source}', Chief."
    
    def move(self, target: str):

        if target.startswith("it|"):

            if runtime_context.last_file:

                target = runtime_context.last_file + "|" + target[3:]

            else:

                return "I don't know what 'it' refers to yet, Chief."
        
        if "|" not in target:
            return "Please specify both file names, Chief."

        source, destination = target.split("|", 1)

        source_path = self._resolve_path(source)
        destination_path = self._resolve_path(destination)

        if self.manager.move(str(source_path), str(destination_path)):
            
            return f"Moved '{source}' to '{destination}', Chief."

        return f"I couldn't find '{source}', Chief."
    
    def delete(self, target: str):

        if target.lower() == "it":

            if runtime_context.last_file:

                target = runtime_context.last_file

            else:

                return "I don't know what 'it' refers to yet, Chief."
        
        target_path = self._resolve_path(target)
        
        
        if self.manager.delete(str(target_path)):
            runtime_context.last_file = None
            return f"Deleted '{target_path.name}', Chief."

        return f"I couldn't find '{target}', Chief."
    
    def read(self, target: str):
        
        if target.lower() == "it":

            if runtime_context.last_file:

                target = runtime_context.last_file

            else:

                return "I don't know what 'it' refers to yet, Chief."

        file_path = self._resolve_path(target)

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
    
    def write(self, target: str, content: str):

        if target.lower() == "it":

            if runtime_context.last_file:
               target = runtime_context.last_file
            else:
               return "I don't know what 'it' refers to yet, Chief."

        file_path = self._resolve_path(target)

        if self.manager.write(str(file_path), content):

            runtime_context.last_file = str(file_path)

            return f"I've written to '{file_path.name}', Chief."

        return f"I couldn't write to '{target}', Chief."
    
    def append(self, target: str, content: str):

        if target.lower() == "it":

            if runtime_context.last_file:
                target = runtime_context.last_file
            else:
                return "I don't know what 'it' refers to yet, Chief."

        file_path = self._resolve_path(target)

        if self.manager.append(str(file_path), content):

            runtime_context.last_file = str(file_path)

            return f"I've appended to '{file_path.name}', Chief."

        return f"I couldn't append to '{target}', Chief."
    
    def replace(self, target: str):

        parts = target.split("|")

        if len(parts) != 3:
            return "Please specify the file, old text, and new text, Chief."

        file_name, old_text, new_text = parts

        if file_name.lower() == "it":

            if runtime_context.last_file:
               file_name = runtime_context.last_file
            else:
               return "I don't know what 'it' refers to yet, Chief."

        file_path = self._resolve_path(file_name)

        success = self.manager.replace(
            str(file_path),
            old_text,
            new_text
        )
        
        if success:

            runtime_context.last_file = str(file_path)

            return (
                f"Replaced '{old_text}' with "
                f"'{new_text}' in '{file_path.name}', Chief."
            )
            

        return f"I couldn't update '{file_name}', Chief."
    
    def clear(self, target: str):

        if target.lower() == "it":

            if runtime_context.last_file:
                target = runtime_context.last_file
            else:
                return "I don't know what 'it' refers to yet, Chief."

        file_path = self._resolve_path(target)

        if self.manager.clear(str(file_path)):

            runtime_context.last_file = str(file_path)

            return f"I've cleared '{file_path.name}', Chief."

        return f"I couldn't clear '{target}', Chief."