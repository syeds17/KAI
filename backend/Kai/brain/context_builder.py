class ContextBuilder:
    """
    Builds conversation context for the LLM.
    """

    def build(self, conversations) -> str:

        if not conversations:
            return ""

        lines = []

        for user, assistant in reversed(conversations):
            lines.append(f"User: {user}")
            lines.append(f"KAI: {assistant}")
            lines.append("")

        return "\n".join(lines)