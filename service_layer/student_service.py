from models.student import Student
from data_layer import student_dao
from reports import report_generator
from service_layer import validators


def _row_to_student(row):
    if not row:
        return None

    return Student(
        student_id=row["student_id"],
        first_name=row["first_name"],
        last_name=row["last_name"],
        email=row["email"],
        major=row["major"],
        year_level=row["year_level"],
        active=bool(row["active"])
    )


def add_student(first_name, last_name, email, major, year_level):
    if (
        not first_name.strip()
        or not last_name.strip()
        or not email.strip()
        or not major.strip()
        or not year_level.strip()
    ):
        return "All fields are required."
    
    if not validators.is_valid_name(first_name):
        return "Invalid first name."

    if not validators.is_valid_name(last_name):
        return "Invalid last name."

    if not validators.is_valid_email(email):
        return "Invalid email format."

    if not validators.is_valid_text_field(major):
        return "Invalid major."

    if not validators.is_valid_text_field(year_level):
        return "Invalid year level."

    try:
        new_id = student_dao.insert_student(
            first_name.strip(),
            last_name.strip(),
            email.strip(),
            major.strip(),
            year_level.strip()
        )
        return f"Student added successfully. New student ID: {new_id}"
    except Exception as e:
        if "Duplicate" in str(e) or "duplicate" in str(e):
            return "Email already exists."
        return f"Error adding student: {e}"


def get_all_students():
    rows = student_dao.fetch_all_students()
    return [_row_to_student(row) for row in rows]


def get_student_by_id(student_id):
    try:
        student_id = int(student_id)
    except ValueError:
        return None

    row = student_dao.fetch_student_by_id(student_id)
    return _row_to_student(row)


def update_student(student_id, first_name, last_name, email, major, year_level):
    try:
        student_id = int(student_id)
    except ValueError:
        return "Student ID must be a number."

    if (
        not first_name.strip()
        or not last_name.strip()
        or not email.strip()
        or not major.strip()
        or not year_level.strip()
    ):
        return "All fields are required."
    
    if not validators.is_valid_name(first_name):
        return "Invalid first name."

    if not validators.is_valid_name(last_name):
        return "Invalid last name."

    if not validators.is_valid_email(email):
        return "Invalid email format."

    if not validators.is_valid_text_field(major):
        return "Invalid major."

    if not validators.is_valid_text_field(year_level):
        return "Invalid year level."

    existing_student = student_dao.fetch_student_by_id(student_id)
    if not existing_student:
        return "Student not found."

    try:
        rows_updated = student_dao.update_student(
            student_id,
            first_name.strip(),
            last_name.strip(),
            email.strip(),
            major.strip(),
            year_level.strip()
        )

        if rows_updated == 0:
            return "Student not found."

        return "Student updated successfully."
    except Exception as e:
        if "Duplicate" in str(e) or "duplicate" in str(e):
            return "Email already exists."
        return f"Error updating student: {e}"


def delete_student(student_id):
    try:
        student_id = int(student_id)
    except ValueError:
        return "Student ID must be a number."

    existing_student = student_dao.fetch_student_by_id(student_id)
    if not existing_student:
        return "Student not found."

    if student_dao.student_has_enrollments(student_id):
        return "Cannot delete student: this student is currently enrolled in one or more courses."

    rows_deleted = student_dao.delete_student(student_id)
    if rows_deleted == 0:
        return "Student not found."

    return "Student removed successfully."

def generate_student_report(student_id):
    try:
        student_id = int(student_id)
    except ValueError:
        return "Student ID must be a number."

    path, error = report_generator.generate_student_enrollment_report(student_id)

    if error:
        return error

    return f"Student report generated successfully!"