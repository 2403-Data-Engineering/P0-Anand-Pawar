from dataclasses import dataclass


@dataclass
class Student:
    student_id: int | None
    first_name: str
    last_name: str
    email: str
    major: str
    year_level: str
    active: bool = True