class RuntimeContext:

    def __init__(self):

        self.reset()

    def reset(self):

        # File context
        self.last_file = None
        self.last_folder = None

        # Search context
        self.last_search = []

        # Navigation
        self.current_directory = None

        # Clipboard-like references
        self.selected_item = None

        # Conversation
        self.last_command = None
        self.last_response = None


runtime_context = RuntimeContext()