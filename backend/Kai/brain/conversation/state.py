class ConversationState:

    def __init__(self):

        self.last_action = None
        self.last_target = None

    def remember(self, command):

        self.last_action = command.action
        self.last_target = command.target


conversation_state = ConversationState()