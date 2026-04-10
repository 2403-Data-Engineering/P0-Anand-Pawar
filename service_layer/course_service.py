from models.course import Course
from data_layer import course_dao, professor_dao
from service_layer import validators 


def _row_to_course(row):
    if not row:
        return None

    return Course(
        course_id=row["course_id"],
        class_name=row["class_name"],
        subject_code=row["subject_code"],
        professor_id=row["professor_id"],
        active=bool(row["active"]),
        professor_name=row.get("professor_name")
    )


def add_course(class_name, subject_code, professor_id):
    if not class_name.strip() or not subject_code.strip() or not str(professor_id).strip():
        return "All fields are required."

    if not validators.is_valid_text_field(class_name):
        return "Invalid Class Name."
    if not validators.is_valid_subject_code(subject_code):
        return "Invalid Subject Code."

    try:
        professor_id = int(professor_id)
    except ValueError:
        return "Professor ID must be a number."

    professor = professor_dao.fetch_professor_by_id(professor_id)
    if not professor:
        return "Professor not found. Course must be assigned to an existing active professor."

    try:
        new_id = course_dao.insert_course(
            class_name.strip(),
            subject_code.strip(),
            professor_id
        )
        return f"Course added successfully. New course ID: {new_id}"
    except Exception as e:
        return f"Error adding course: {e}"


def get_all_courses():
    rows = course_dao.fetch_all_courses()
    return [_row_to_course(row) for row in rows]


def get_course_by_id(course_id):
    try:
        course_id = int(course_id)
    except ValueError:
        return None

    row = course_dao.fetch_course_by_id(course_id)
    return _row_to_course(row)


def update_course(course_id, class_name, subject_code, professor_id):
    try:
        course_id = int(course_id)
    except ValueError:
        return "Course ID must be a number."

    if not class_name.strip() or not subject_code.strip() or not str(professor_id).strip():
        return "All fields are required."
    
    if not validators.is_valid_text_field(class_name):
        return "Invalid Class Name."
    if not validators.is_valid_subject_code(subject_code):
        return "Invalid Subject Code."

    try:
        professor_id = int(professor_id)
    except ValueError:
        return "Professor ID must be a number."

    existing_course = course_dao.fetch_course_by_id(course_id)
    if not existing_course:
        return "Course not found."

    professor = professor_dao.fetch_professor_by_id(professor_id)
    if not professor:
        return "Professor not found. Course must be assigned to an existing active professor."

    try:
        rows_updated = course_dao.update_course(
            course_id,
            class_name.strip(),
            subject_code.strip(),
            professor_id
        )

        if rows_updated == 0:
            return "Course not found."

        return "Course updated successfully."
    except Exception as e:
        return f"Error updating course: {e}"


def delete_course(course_id):
    try:
        course_id = int(course_id)
    except ValueError:
        return "Course ID must be a number."

    existing_course = course_dao.fetch_course_by_id(course_id)
    if not existing_course:
        return "Course not found."

    if course_dao.course_has_enrollments(course_id):
        return "Cannot delete course: students are still enrolled in this course."

    rows_deleted = course_dao.delete_course(course_id)
    if rows_deleted == 0:
        return "Course not found."

    return "Course removed successfully."