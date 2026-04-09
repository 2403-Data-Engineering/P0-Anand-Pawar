from data_layer import enrollment_dao, student_dao, course_dao


def enroll_student_in_course(student_id, course_id):
    try:
        student_id = int(student_id)
    except ValueError:
        return "Student ID must be a number."

    try:
        course_id = int(course_id)
    except ValueError:
        return "Course ID must be a number."

    student = student_dao.fetch_student_by_id(student_id)
    if not student:
        return "Student not found."

    course = course_dao.fetch_course_by_id(course_id)
    if not course:
        return "Course not found."

    if enrollment_dao.enrollment_exists(student_id, course_id):
        return "This student is already enrolled in this course."

    try:
        enrollment_dao.insert_enrollment(student_id, course_id)
        return "Student enrolled successfully."
    except Exception as e:
        return f"Error enrolling student: {e}"


def drop_student_from_course(student_id, course_id):
    try:
        student_id = int(student_id)
    except ValueError:
        return "Student ID must be a number."

    try:
        course_id = int(course_id)
    except ValueError:
        return "Course ID must be a number."

    if not enrollment_dao.enrollment_exists(student_id, course_id):
        return "Enrollment not found."

    rows_deleted = enrollment_dao.delete_enrollment(student_id, course_id)
    if rows_deleted == 0:
        return "Enrollment not found."

    return "Student dropped from course successfully."


def get_students_by_course(course_id):
    try:
        course_id = int(course_id)
    except ValueError:
        return [], "Course ID must be a number."

    course = course_dao.fetch_course_by_id(course_id)
    if not course:
        return [], "Course not found."

    students = enrollment_dao.fetch_students_by_course(course_id)
    return students, None


def get_courses_by_student(student_id):
    try:
        student_id = int(student_id)
    except ValueError:
        return [], "Student ID must be a number."

    student = student_dao.fetch_student_by_id(student_id)
    if not student:
        return [], "Student not found."

    courses = enrollment_dao.fetch_courses_by_student(student_id)
    return courses, None