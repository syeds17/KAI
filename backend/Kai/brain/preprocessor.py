class Preprocessor:
    """
    Converts natural language into clean commands
    that KAI's parser can understand.
    """

    def __init__(self):

        # -------------------------------------------------
        # Multi-word phrase replacements
        # -------------------------------------------------

        self.phrase_replacements = {

            "i want you to": "",
            "i want to": "",
            "would you mind": "",
            "can you": "",
            "could you": "",
            "will you": "",
            "please": "",
            "kindly": "",
            "do me a favor and": "",
            "do a favor and": "",
            "help me": "",
            "help": "",
            "try to": "",
            "go ahead and": "",
        }

        # -------------------------------------------------
        # Words to completely remove
        # -------------------------------------------------

        self.remove_words = {

            "the",
            "a",
            "an",

            "my",
            "your",
            "our",

            "me",
            "you",

            "for",
            "to",
            "of",
            "on",
            "in",
            "at",

            "is",
            "are",
            "was",
            "were",
            "be",
            "been",
            "being",

            "just",
            "simply",
            "actually",
            "really",
            "now",
            "then",

            "that",
            "this",
        }

        # -------------------------------------------------
        # Verb normalization
        # -------------------------------------------------

        self.verb_map = {

            # OPEN

            "opening": "open",
            "opened": "open",
            "opens": "open",

            "launch": "open",
            "launching": "open",
            "launched": "open",

            "start": "open",
            "starting": "open",
            "started": "open",

            "run": "open",
            "running": "open",

            # CLOSE

            "closing": "close",
            "closed": "close",
            "closes": "close",

            "terminate": "close",
            "terminating": "close",

            "kill": "close",
            "killing": "close",

            "exit": "close",
            "quit": "close",

            # SEARCH

            "find": "search",
            "finding": "search",
            "found": "search",

            "locate": "search",
            "locating": "search",

            "lookup": "search",
            "looking": "search",

            "searching": "search",
            "searched": "search",

            # CREATE

            "create": "create",
            "creating": "create",
            "created": "create",

            "make": "create",
            "making": "create",
            "made": "create",

            "generate": "create",
            "generating": "create",

            # DELETE

            "remove": "delete",
            "removing": "delete",

            "delete": "delete",
            "deleting": "delete",
            "deleted": "delete",

            # COPY

            "copying": "copy",
            "copied": "copy",

            # MOVE

            "moving": "move",
            "moved": "move",

            # RENAME

            "renaming": "rename",
            "renamed": "rename",

            # READ

            "reading": "read",
            "reads": "read",

            # PLAY

            "playing": "play",
            "played": "play",
        }

        # -------------------------------------------------
        # Words that don't help parsing
        # -------------------------------------------------

        self.ignore_words = {

            "browser",
            "application",
            "software",
            "app",
            "program",
            "directory",

            "named",
            "called",

            "new",
        }

        # -------------------------------------------------
        # Spoken numbers
        # -------------------------------------------------

        self.number_map = {

            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "ten": "10",
        }

    def clean(self, text: str) -> str:

        text = text.lower().strip()

        # Replace common phrases

        for phrase, replacement in self.phrase_replacements.items():

            text = text.replace(phrase, replacement)

        words = text.split()

        cleaned = []

        for word in words:

            # Convert spoken numbers

            word = self.number_map.get(word, word)

            # Normalize verbs

            word = self.verb_map.get(word, word)

            # Remove filler words

            if word in self.remove_words:
                continue

            # Ignore unnecessary nouns

            if word in self.ignore_words:
                continue

            cleaned.append(word)

        return " ".join(cleaned)