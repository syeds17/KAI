from dataclasses import dataclass


@dataclass
class Command:
    action: str
    target: str
    raw: str