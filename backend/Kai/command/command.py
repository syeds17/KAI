from dataclasses import dataclass


@dataclass
class Command:

    action: str
    target: str = ""
    raw: str = ""

    # Used by write/append commands
    content: str = ""

    # Future-proofing (optional but useful)
    source: str = ""
    destination: str = ""