from command.command import Command

from .pending_action import PendingAction
from .slot_filler import SlotFiller
from .context_resolver import ContextResolver
from .extractor import SlotExtractor
from .state import conversation_state


class ConversationManager:

    def __init__(self):

        self.pending = PendingAction()
        self.slot_filler = SlotFiller()
        self.context = ContextResolver()
        self.extractor = SlotExtractor()
        self.state = conversation_state

    def handle(self, command: Command):

        # Resolve words like:
        # "it", "there", "inside it"
        command = self.context.resolve(command, self.pending)

        if self.pending.active():

            for slot in self.pending.missing():

                value = self.extractor.extract(slot, command.raw)

                if value:
                    self.pending.fill(slot, value)

            if self.pending.missing():

                return None, "I'm still missing some information, Chief."

            new_command = Command(
                action=self.pending.action,
                target=self.pending.get("target") or self.pending.get("name") or "",
                content=self.pending.get("content") or "",
                raw=command.raw
            )
            
            self.state.remember(new_command)

            self.pending.clear()

            return new_command, None

        if command.action == "create_folder" and not command.target:

            self.pending.set(
                "create_folder",
                {
                    "name": None,
                    "folder": None,
                    "extension": None
                }
            )

            return None, "What would you like to name the folder, Chief?"

        if command.action == "create_file" and not command.target:

            self.pending.set(
                "create_file",
                {
                    "target": None
                }
            )

            return None, "What would you like to name the file, Chief?"


        if command.action == "write":

            if command.content and command.target:
                self.state.remember(command)
                return command, None

            self.pending.set(
                "write",
                {
                    "content": command.content or None,
                    "target": command.target or None,
                }
            )
            return None, self._next_question()

        if command.action == "append":

            self.pending.set(
                "append",
               {
                   "content": command.content or None,
                   "target": command.target or None,
                }
            )

            return None, self._next_question()

        if command.action == "clear":

            self.pending.set(
                "clear",
               {
                        "target": command.target or None,
                }
            )

            return None, self._next_question()

        if command.action == "replace":

            parts = command.target.split("|")

            target = parts[0] if len(parts) > 0 else None
            old = parts[1] if len(parts) > 1 else None
            new = parts[2] if len(parts) > 2 else None

            self.pending.set(
                "replace",
                {
                    "target": target,
                    "old": old,
                    "new": new,
                }
            )

            return None, self._next_question()
        
        self.state.remember(command)
        
        return command, None

    def _next_question(self):

        if not self.pending.missing():
            return None

        slot = self.pending.missing()[0]

        questions = {

            "name": "What would you like to call it, Chief?",

            "target": "Which file should I use, Chief?",

            "content": "What would you like me to write, Chief?",

            "folder": "Which folder should I use, Chief?",

            "extension": "Which file extension should I use, Chief?",
            
            "old": "What text should I replace, Chief?",

            "new": "What should I replace it with, Chief?"
        }

        return questions.get(
            slot,
            "I'm still missing some information, Chief."
        )