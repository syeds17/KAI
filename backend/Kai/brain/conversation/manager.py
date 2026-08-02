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
        self.state = conversation_state()

    def handle(self, command: Command):

        # Resolve words like:
        # "it", "there", "inside it"
        command = self.context.resolve(command, self.pending)

        # -------------------------------
        # Continue existing conversation
        # -------------------------------
        if self.pending.active():

            for slot in self.pending.missing():

                value = self.extractor.extract(slot, command.raw)

                if value:
                    self.pending.fill(slot, value)

            if self.pending.missing():

                return None, "I'm still missing some information, Chief."

            new_command = Command(
                action=self.pending.action,
                target=self.pending.get("name"),
                raw=command.raw
            )
            
            self.state.remember(new_command)

            self.pending.clear()

            return new_command, None

        # -------------------------------
        # Start new conversations
        # -------------------------------

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
                    "name": None
                }
            )

            return None, "What would you like to name the file, Chief?"
        
        self.state.remember(command)
        
        return command, None

    def _next_question(self):

        if self.pending.action == "create_folder":

            return "What would you like to name the folder, Chief?"

        if self.pending.action == "create_file":

            return "What would you like to name the file, Chief?"

        return "I'm still missing some information, Chief."