class CommandSplitter:
    """
    Splits multi-step requests into individual commands.
    """

    def plan(self, text: str):

        separators = [
            " and then ",
            " then ",
            " after that ",
            " and "
        ]

        commands = [text]

        for separator in separators:

            new_commands = []

            for command in commands:
                new_commands.extend(command.split(separator))

            commands = new_commands

        return [
            command.strip()
            for command in commands
            if command.strip()
        ]