from models.student import Student

_students = []
_next_id = 1


def add_student(first_name, last_name, major):
    global _next_id

    new_student = Student(
        id=_next_id,
        first_name=first_name,
        last_name=last_name,
        major=major
    )

    _students.append(new_student)
    _next_id += 1

    return new_student


def get_all_students():
    return _students


def get_student_by_id(student_id):
    try:
        student_id = int(student_id)
    except ValueError:
        return None

    for student in _students:
        if student.id == student_id:
            return student
    return None


def update_student(student_id, first_name, last_name, major):
    student = get_student_by_id(student_id)

    if not student:
        return None

    if first_name:
        student.first_name = first_name
    if last_name:
        student.last_name = last_name
    if major:
        student.major = major

    return student


def delete_student(student_id):
    global _students

    student = get_student_by_id(student_id)

    if not student:
        return False

    _students = [s for s in _students if s.id != student.id]

    return True