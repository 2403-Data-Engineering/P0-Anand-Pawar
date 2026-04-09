from service_layer import student_service


def _print_students(students):
    if not students:
        print("\nNo students found.\n")
        return

    print("\n--- Students List ---")
    for student in students:
        print(
            f"{student.student_id}. "
            f"{student.first_name} {student.last_name} | "
            f"Email: {student.email} | "
            f"Major: {student.major} | "
            f"Year: {student.year_level}"
        )
    print()


def student_menu():
    while True:
        print("\nStudent Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Generate Student Report")
        print("6. Back to Main Menu")

        choice = input("Enter your choice (1/2/3/4/5/6): ").strip()

        if choice == "1":
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            email = input("Email: ").strip()
            major = input("Major: ").strip()
            year_level = input("Year Level: ").strip()

            message = student_service.add_student(
                first_name,
                last_name,
                email,
                major,
                year_level
            )
            print(message)

        elif choice == "2":
            students = student_service.get_all_students()
            _print_students(students)

        elif choice == "3":
            student_id = input("Enter Student ID to update: ").strip()

            existing_student = student_service.get_student_by_id(student_id)
            if not existing_student:
                print("Student not found.")
                continue

            print("\nLeave blank to keep the current value.\n")

            first_name = input(f"New First Name [{existing_student.first_name}]: ").strip()
            last_name = input(f"New Last Name [{existing_student.last_name}]: ").strip()
            email = input(f"New Email [{existing_student.email}]: ").strip()
            major = input(f"New Major [{existing_student.major}]: ").strip()
            year_level = input(f"New Year Level [{existing_student.year_level}]: ").strip()

            if first_name == "":
                first_name = existing_student.first_name
            if last_name == "":
                last_name = existing_student.last_name
            if email == "":
                email = existing_student.email
            if major == "":
                major = existing_student.major
            if year_level == "":
                year_level = existing_student.year_level

            message = student_service.update_student(
                student_id,
                first_name,
                last_name,
                email,
                major,
                year_level
            )
            print(message)

        elif choice == "4":
            student_id = input("Enter Student ID to delete: ").strip()
            message = student_service.delete_student(student_id)
            print(message)

        elif choice == "5":
            student_id = input("Enter Student ID to generate their Markdown Report (or 'b' to go back): ").strip()
            
            if student_id.lower() == "b":
                continue

            existing_student = student_service.get_student_by_id(student_id)
            if not existing_student:
                print("Student not found.")
                continue

            message = student_service.generate_student_report(student_id)
            print(message)
        
        elif choice == "6":
            return "main"

        else:
            print("Invalid choice, please try again.")