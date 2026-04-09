from dataclasses import dataclass

@dataclass
class Professor:
    professor_id: int | None
    first_name: str
    last_name: str
    department: str
    email: str
    active: bool = True




    