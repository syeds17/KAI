from .parameter_extractor import ParameterExtractor


class SlotFiller:

    def __init__(self):

        self.extractor = ParameterExtractor()

    def fill(self, pending, command):

        if not pending.active():
            return

        for slot in pending.missing():

            if slot == "name":

                value = self.extractor.extract_name(command.raw)

            elif slot == "target":

                value = self.extractor.extract_name(command.raw)

            elif slot == "content":

                value = command.raw.strip()

            elif slot == "folder":

                value = self.extractor.extract_name(command.raw)

            elif slot == "extension":

                value = self.extractor.extract_name(command.raw)

            elif slot == "old":

                value = self.extractor.extract_name(command.raw)

            elif slot == "new":

                value = self.extractor.extract_name(command.raw)

            else:

                value = None

            if value:
                pending.fill(slot, value)