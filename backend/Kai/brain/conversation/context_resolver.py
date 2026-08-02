from brain.runtime_context import runtime_context


class ContextResolver:

    def resolve(self, command, pending):

        target = command.target.lower()

        if target == "it":

            if runtime_context.last_file:

                command.target = runtime_context.last_file

        elif target == "there":

            if runtime_context.last_folder:

                command.target = runtime_context.last_folder

        return command