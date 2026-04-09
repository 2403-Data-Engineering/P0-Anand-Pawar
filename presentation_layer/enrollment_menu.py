from service_layer import enrollment_service


def _print_students_in_course(students, course_id):
    print(f"\n--- Students in Course {course_id} ---")
    if not students:
        print("No students enrolled in this course.\n")
        return

    for student in students:
        print(
            f"{student['student_id']}. "
            f"{student['first_name']} {student['last_name']} | "
            f"Email: {student['email']} | "
            f"Major: {student['major']} | "
            f"Year: {student['year_level']}"
        )
    print()


def _print_courses_for_student(courses, student_id):
    print(f"\n--- Courses for Student {student_id} ---")
    if not courses:
        print("This student is not enrolled in any courses.\n")
        return

    for course in courses:
        professor_name = course["professor_name"] if course["professor_name"] else "Unknown Professor"
        print(
            f"{course['course_id']}. "
            f"{course['class_name']} | "
            f"Code: {course['subject_code']} | "
            f"Professor: {professor_name}"
        )
    print()


def enrollment_menu():
    while True:
        print("\nEnrollment Management")
        print("1. Enroll Student in Course")
        print("2. Drop Student from Course")
        print("3. View Students in a Course")
        print("4. View Courses for a Student")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip()
            course_id = input("Course ID: ").strip()

            message = enrollment_service.enroll_student_in_course(student_id, course_id)
            print(message)

        elif choice == "2":
            student_id = input("Student ID: ").strip()
            course_id = input("Course ID: ").strip()

            message = enrollment_service.drop_student_from_course(student_id, course_id)
            print(message)

        elif choice == "3":
            course_id = input("Enter Course ID: ").strip()
            students, error = enrollment_service.get_students_by_course(course_id)

            if error:
                print(error)
                continue

            _print_students_in_course(students, course_id)

        elif choice == "4":
            student_id = input("Enter Student ID: ").strip()
            courses, error = enrollment_service.get_courses_by_student(student_id)

            if error:
                print(error)
                continue

            _print_courses_for_student(courses, student_id)

        elif choice == "5":
            return "main"

        else:
            print("Invalid choice, please try again.")