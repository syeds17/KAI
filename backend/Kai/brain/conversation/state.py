class ConversationState:

    def __init__(self):

        self.last_action = None
        self.last_target = None
        self.last_folder = None
        self.last_file = None

    def remember(self, command):

        self.last_action = command.action
        self.last_target = command.target

        if command.action == "create_folder":
            self.last_folder = command.target

        if command.action == "create_file":
            self.last_file = command.target


conversation_state = ConversationState()