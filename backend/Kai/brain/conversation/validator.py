from command.command import Command
from ..runtime_context import pending_action


class Validator:
    """
    Validates parsed commands before execution.
    """

    def validate(self, command: Command):

        action = command.action
        target = command.target.strip()

        # ---------- CREATE ----------
        if action == "create_folder":

            if not target:
                pending_action.set("create_folder", "folder_name")
                return "What would you like to name the folder, Chief."

        if action == "create_file":

            if not target:
                pending_action.set("create_file", "file_name")
                return "What would you like to name the file, Chief."

        # ---------- OPEN ----------
        if action == "open":

            if not target:
                return "What would you like me to open, Chief."

        # ---------- CLOSE ----------
        if action == "close":

            if not target:
                return "Which application would you like me to close, Chief."

        # ---------- SEARCH ----------
        if action == "search":

            if not target:
                return "What would you like me to search for, Chief."

        # ---------- READ ----------
        if action == "read":

            if not target:
                return "Which file would you like me to read, Chief."

        # ---------- DELETE ----------
        if action == "delete":

            if not target:
                return "Which file should I delete, Chief."

        # ---------- COPY ----------
        if action == "copy":

            if not target:
                return "Please tell me what you'd like to copy, Chief."

        # ---------- MOVE ----------
        if action == "move":

            if not target:
                return "Please tell me what you'd like to move, Chief."

        # ---------- RENAME ----------
        if action == "rename":

            if "|" not in target:
                return (
                    "Please tell me both the old and new names, Chief.\n"
                    "Example: rename notes.txt|ideas.txt"
                )

        return None