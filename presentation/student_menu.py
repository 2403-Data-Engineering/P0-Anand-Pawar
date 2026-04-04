# presentation/student_menu.py

from services import student_service


def student_menu():
    while True:
        print("Student Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: (1/2/3/4/5) ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice, please try again.")
            continue

        # --- ADD STUDENT ---
        elif choice == '1':
            first = input("First Name: ")
            last = input("Last Name: ")
            major = input("Major: ")

            student = student_service.add_student(first, last, major)

            print(f"\nStudent {student.first_name} {student.last_name} added successfully!\n")

        # --- VIEW STUDENTS + SELECT ---
        elif choice == '2':
            print("\n--- Students List ---")

            students = student_service.get_all_students()

            if not students:
                print("No students found.")
                continue

            for s in students:
                print(f"{s.id}. {s.first_name} {s.last_name} ({s.major})")

            student_id = input("\nEnter Student ID for report (or 'b' to go back): ")

            if student_id.lower() == 'b':
                continue

            if not student_id.isdigit():
                print("Invalid ID")
                continue

            student = student_service.get_student_by_id(student_id)

            if not student:
                print("Student not found.")
                continue

            print(f"\nSelected: {student.first_name} {student.last_name}\n")

        # --- UPDATE STUDENT ---
        elif choice == '3':
            student_id = input("Enter Student ID to update: ")

            if not student_id.isdigit():
                print("Invalid ID")
                continue

            print("Enter updates (leave blank to keep same):")

            first = input("Updated First Name: ")
            last = input("Updated Last Name: ")
            major = input("Updated Major: ")

            student = student_service.update_student(student_id, first, last, major)

            if student:
                print(f"\nStudent {student.id} updated successfully!\n")
            else:
                print("Student not found.")

        # --- DELETE STUDENT ---
        elif choice == '4':
            student_id = input("Enter Student ID to delete: ")

            if not student_id.isdigit():
                print("Invalid ID")
                continue

            success = student_service.delete_student(student_id)

            if success:
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        # --- BACK ---
        elif choice == '5':
            return "main"