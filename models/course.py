from dataclasses import dataclass


@dataclass
class Course:
    course_id: int | None
    class_name: str
    subject_code: str
    professor_id: int
    active: bool = True
    professor_name: str | None = None