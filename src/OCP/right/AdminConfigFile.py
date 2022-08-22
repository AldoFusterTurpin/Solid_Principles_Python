from dataclasses import dataclass


@dataclass
class AdminConfigFile:
    name: str
    content: str
