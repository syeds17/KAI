from .parameter_extractor import ParameterExtractor


class SlotFiller:

    def __init__(self):

        self.extractor = ParameterExtractor()

    def fill(self, pending, command):

        if not pending.active():
            return

        if "name" in pending.missing():

            name = self.extractor.extract_name(command.raw)

            if name:
                pending.fill("name", name)