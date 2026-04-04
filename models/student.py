from dataclasses import dataclass

@dataclass
class Student:
    id: int | None
    first_name: str
    last_name: str
    major: str