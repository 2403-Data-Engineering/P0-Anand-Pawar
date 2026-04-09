from service_layer import professor_service


def _print_professors(professors):
    if not professors:
        print("\nNo professors found.\n")
        return

    print("\n--- Professors List ---")
    for professor in professors:
        print(
            f"{professor.professor_id}. "
            f"{professor.first_name} {professor.last_name} | "
            f"Department: {professor.department} | "
            f"Email: {professor.email}"
        )
    print()


def professor_menu():
    while True:
        print("\nProfessor Management")
        print("1. Add Professor")
        print("2. View Professors")
        print("3. Update Professor")
        print("4. Delete Professor")
        print("5. Generate Professor Report")
        print("6. Back to Main Menu")

        choice = input("Enter your choice (1/2/3/4/5): ").strip()

        if choice == "1":
            first_name = input("First Name: ").strip()
            last_name = input("Last Name: ").strip()
            department = input("Department: ").strip()
            email = input("Email: ").strip()

            message = professor_service.add_professor(first_name, last_name, department, email)
            print(message)

        elif choice == "2":
            professors = professor_service.get_all_professors()
            _print_professors(professors)

        elif choice == "3":
            professor_id = input("Enter Professor ID to update: ").strip()

            existing_professor = professor_service.get_professor_by_id(professor_id)
            if not existing_professor:
                print("Professor not found.")
                continue

            print("\nLeave blank to keep the current value.\n")

            first_name = input(f"New First Name [{existing_professor.first_name}]: ").strip()
            last_name = input(f"New Last Name [{existing_professor.last_name}]: ").strip()
            department = input(f"New Department [{existing_professor.department}]: ").strip()
            email = input(f"New Email [{existing_professor.email}]: ").strip()

            if first_name == "":
                first_name = existing_professor.first_name
            if last_name == "":
                last_name = existing_professor.last_name
            if department == "":
                department = existing_professor.department
            if email == "":
                email = existing_professor.email

            message = professor_service.update_professor(
                professor_id,
                first_name,
                last_name,
                department,
                email
            )
            print(message)

        elif choice == "4":
            professor_id = input("Enter Professor ID to delete: ").strip()
            message = professor_service.delete_professor(professor_id)
            print(message)

        elif choice == "5":

            professor_id = input("Enter Professor ID to generate a report (or 'b' to go back): ").strip()

            if professor_id.lower() == "b":
                continue

            existing_professor = professor_service.get_professor_by_id(professor_id)
            if not existing_professor:
                print("Professor not found.")
                continue

            message = professor_service.generate_professor_report(professor_id)
            print(message)

        elif choice == "6":
            return "main"

        else:
            print("Invalid choice, please try again.")