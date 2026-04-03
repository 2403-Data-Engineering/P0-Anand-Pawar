from models.professor import Professor

# temporary in-memory storage (replace with DB later)
_professors = []
_next_id = 1


def add_professor(first_name, last_name, dept):
    global _next_id

    new_prof = Professor(
        id=_next_id,
        first_name=first_name,
        last_name=last_name,
        dept=dept
    )

    _professors.append(new_prof)
    _next_id += 1

    print(f"\nProfessor added: {new_prof}")
    return new_prof


def get_all_professors():
    return _professors


def get_professor_by_id(prof_id):
    for prof in _professors:
        if prof.id == int(prof_id):
            return prof
    return None


def update_professor(prof_id, first_name, last_name, dept):
    prof = get_professor_by_id(prof_id)

    if not prof:
        print("Professor not found.")
        return None

    prof.first_name = first_name
    prof.last_name = last_name
    prof.dept = dept

    print(f"\nProfessor updated: {prof}")
    return prof


def delete_professor(prof_id):
    global _professors

    prof = get_professor_by_id(prof_id)

    if not prof:
        print("Professor not found.")
        return False

    _professors = [p for p in _professors if p.id != int(prof_id)]

    print(f"\nProfessor {prof_id} deleted.")
    return True