from service_layer import course_service


def _print_courses(courses):
    if not courses:
        print("\nNo courses found.\n")
        return

    print("\n--- Courses List ---")
    for course in courses:
        professor_name = course.professor_name if course.professor_name else "Unknown Professor"
        print(
            f"{course.course_id}. "
            f"{course.class_name} | "
            f"Code: {course.subject_code} | "
            f"Professor: {professor_name}"
        )
    print()


def course_menu():
    while True:
        print("\nCourse Management")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Update Course")
        print("4. Delete Course")
        print("5. Back to Main Menu")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            class_name = input("Class Name: ").strip()
            subject_code = input("Subject Code: ").strip()
            professor_id = input("Professor ID: ").strip()

            message = course_service.add_course(class_name, subject_code, professor_id)
            print(message)

        elif choice == "2":
            courses = course_service.get_all_courses()
            _print_courses(courses)

        elif choice == "3":
            course_id = input("Enter Course ID to update: ").strip()

            existing_course = course_service.get_course_by_id(course_id)
            if not existing_course:
                print("Course not found.")
                continue

            print("\nLeave blank to keep the current value.\n")

            class_name = input(f"New Class Name [{existing_course.class_name}]: ").strip()
            subject_code = input(f"New Subject Code [{existing_course.subject_code}]: ").strip()
            professor_id = input(f"New Professor ID [{existing_course.professor_id}]: ").strip()

            if class_name == "":
                class_name = existing_course.class_name
            if subject_code == "":
                subject_code = existing_course.subject_code
            if professor_id == "":
                professor_id = existing_course.professor_id

            message = course_service.update_course(
                course_id,
                class_name,
                subject_code,
                professor_id
            )
            print(message)

        elif choice == "4":
            course_id = input("Enter Course ID to delete: ").strip()
            message = course_service.delete_course(course_id)
            print(message)

        elif choice == "5":
            return "main"

        else:
            print("Invalid choice, please try again.")