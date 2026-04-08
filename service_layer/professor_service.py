from models.professor import Professor
from data_layer import professor_dao

def _row_to_professor(row):
    if not row:
        return None

    return Professor(
        professor_id=row["professor_id"],
        first_name=row["first_name"],
        last_name=row["last_name"],
        department=row["department"],
        email=row["email"],
        active=bool(row["active"])
    )

def add_professor(first_name, last_name, department, email):
    if not first_name.strip() or not last_name.strip() or not department.strip() or not email.strip():
        return "All fields are required."

    try:
        new_id = professor_dao.insert_professor(
            first_name.strip(),
            last_name.strip(),
            department.strip(),
            email.strip()
        )
        return f"Professor added successfully. New professor ID: {new_id}"
    except Exception as e:
        if "Duplicate" in str(e) or "duplicate" in str(e):
            return "Email already exists."
        return f"Error adding professor: {e}"


def get_all_professors():
    rows = professor_dao.fetch_all_professors()
    return [_row_to_professor(row) for row in rows]


def get_professor_by_id(professor_id):
    try:
        professor_id = int(professor_id)
    except ValueError:
        return None

    row = professor_dao.fetch_professor_by_id(professor_id)
    return _row_to_professor(row)


def update_professor(professor_id, first_name, last_name, department, email):
    try:
        professor_id = int(professor_id)
    except ValueError:
        return "Professor ID must be a number."

    if not first_name.strip() or not last_name.strip() or not department.strip() or not email.strip():
        return "All fields are required."

    existing_professor = professor_dao.fetch_professor_by_id(professor_id)
    if not existing_professor:
        return "Professor not found."

    try:
        rows_updated = professor_dao.update_professor(
            professor_id,
            first_name.strip(),
            last_name.strip(),
            department.strip(),
            email.strip()
        )

        if rows_updated == 0:
            return "Professor not found."

        return "Professor updated successfully."
    except Exception as e:
        if "Duplicate" in str(e) or "duplicate" in str(e):
            return "Email already exists."
        return f"Error updating professor: {e}"


def delete_professor(professor_id):
    try:
        professor_id = int(professor_id)
    except ValueError:
        return "Professor ID must be a number."

    existing_professor = professor_dao.fetch_professor_by_id(professor_id)
    if not existing_professor:
        return "Professor not found."

    if professor_dao.professor_has_courses(professor_id):
        return "Cannot delete professor: this professor is still assigned to one or more courses."

    rows_deleted = professor_dao.delete_professor(professor_id)
    if rows_deleted == 0:
        return "Professor not found."

    return "Professor removed successfully."