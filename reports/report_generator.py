import os
from mdutils.mdutils import MdUtils

from data_layer import student_dao, professor_dao, course_dao, enrollment_dao


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "generated_reports")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def _add_markdown_table(md, headers, rows):
    header_line = "| " + " | ".join(str(h) for h in headers) + " |"
    separator_line = "| " + " | ".join(["---"] * len(headers)) + " |"

    md.new_line(header_line)
    md.new_line(separator_line)

    for row in rows:
        row_line = "| " + " | ".join("" if cell is None else str(cell) for cell in row) + " |"
        md.new_line(row_line)

    md.new_line()


def generate_student_enrollment_report(student_id):
    student = student_dao.fetch_student_by_id(student_id)
    if not student:
        return None, "Student not found."

    courses = enrollment_dao.fetch_courses_by_student(student_id)

    file_name = os.path.join(OUTPUT_DIR, f"student_enrollment_report_{student_id}")
    md = MdUtils(file_name=file_name)

    md.new_header(level=1, title="Student Enrollment Report")

    md.new_header(level=2, title="Student Information")
    _add_markdown_table(
        md,
        ["Student ID", "First Name", "Last Name", "Email", "Major", "Year Level"],
        [[
            student["student_id"],
            student["first_name"],
            student["last_name"],
            student["email"],
            student["major"],
            student["year_level"]
        ]]
    )

    md.new_header(level=2, title="Enrolled Courses")

    if not courses:
        md.new_line("This student is not enrolled in any active courses.")
        md.new_line()
    else:
        course_rows = []
        for course in courses:
            professor_name = course["professor_name"] if course["professor_name"] else "Unknown Professor"
            course_rows.append([
                course["course_id"],
                course["class_name"],
                course["subject_code"],
                professor_name
            ])

        _add_markdown_table(
            md,
            ["Course ID", "Class Name", "Subject Code", "Professor"],
            course_rows
        )

    path = md.create_md_file()
    return path, None


def generate_professor_summary_report(professor_id):
    professor = professor_dao.fetch_professor_by_id(professor_id)
    if not professor:
        return None, "Professor not found."

    courses = course_dao.fetch_courses_by_professor(professor_id)

    file_name = os.path.join(OUTPUT_DIR, f"professor_summary_report_{professor_id}")
    md = MdUtils(file_name=file_name)

    md.new_header(level=1, title="Professor Summary Report")

    md.new_header(level=2, title="Professor Information")
    _add_markdown_table(
        md,
        ["Professor ID", "First Name", "Last Name", "Department", "Email"],
        [[
            professor["professor_id"],
            professor["first_name"],
            professor["last_name"],
            professor["department"],
            professor["email"]
        ]]
    )

    md.new_header(level=2, title="Courses Taught")

    if not courses:
        md.new_line("This professor is not teaching any active courses.")
        md.new_line()
    else:
        course_summary_rows = []
        for course in courses:
            students = enrollment_dao.fetch_students_by_course(course["course_id"])
            course_summary_rows.append([
                course["course_id"],
                course["class_name"],
                course["subject_code"],
                len(students)
            ])

        _add_markdown_table(
            md,
            ["Course ID", "Class Name", "Subject Code", "Enrolled Students"],
            course_summary_rows
        )

        md.new_header(level=2, title="Students by Course")

        for course in courses:
            md.new_header(
                level=3,
                title=f"{course['class_name']} ({course['subject_code']})"
            )

            students = enrollment_dao.fetch_students_by_course(course["course_id"])

            if not students:
                md.new_line("No students enrolled.")
                md.new_line()
            else:
                student_rows = []
                for student in students:
                    student_rows.append([
                        student["student_id"],
                        student["first_name"],
                        student["last_name"],
                        student["email"],
                        student["major"],
                        student["year_level"]
                    ])

                _add_markdown_table(
                    md,
                    ["Student ID", "First Name", "Last Name", "Email", "Major", "Year"],
                    student_rows
                )

    path = md.create_md_file()
    return path, None