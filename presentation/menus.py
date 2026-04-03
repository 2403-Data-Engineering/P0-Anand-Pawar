def main_menu():

    print("Welcome Admin!")
    print("This is the University Management System, please select an option:")
    print("1. Manage Professors")
    print("2. Manage Students")
    print("3. Manage Courses")
    print("4. Manage Enrollments")
    print("5. Exit")
    choice = input("Enter your choice: (1/2/3/4/5) ")
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice, please try again.")
    
    return choice

##
##TODO: CREATE OWN CLASS
##
def professor_menu():
    while True:
        print("Professor Management")
        print("1. Add Professor")
        print("2. View Professors")
        print("3. Update Professor")
        print("4. Delete Professor")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: (1/2/3/4/5) ")
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice, please try again.")
            continue
        
        # --- ADD PROFESSOR ---
        if choice == '1':
            first = input("First Name: ")
            last = input("Last Name: ")
            dept = input("Department: ")

            # later → call service layer here
            print(f"\nProfessor {first} {last} added successfully!\n")

        # --- VIEW PROFESSORS + NESTED REPORT ---
        elif choice == '2':
            print("\n--- Professors List ---")

            # TEMP: replace with service call later
            professors = [
                {"id": 1, "name": "John Smith"},
                {"id": 2, "name": "Jane Doe"}
            ]

            for p in professors:
                print(f"{p['id']}. {p['name']}")

            prof_id = input("\nEnter Professor ID to select (or 'b' to go back): ")

            if prof_id.lower() == 'b':
                continue

            # nested submenu
            while True:
                print(f"\nSelected Professor ID: {prof_id}")
                print("1. Generate Report")
                print("2. Back")

                sub_choice = input("Enter choice: ")

                if sub_choice == '1':
                    # later → call report service
                    print(f"Generating report for professor {prof_id}...\n")

                elif sub_choice == '2':
                    break

                else:
                    print("Invalid choice.")

        # --- UPDATE PROFESSOR ---
        elif choice == '3':
            prof_id = input("Enter Professor ID to update: ")
            print(f"Updating Professor {prof_id} (stub)\n")

        # --- DELETE PROFESSOR ---
        elif choice == '4':
            prof_id = input("Enter Professor ID to delete: ")
            print(f"Deleting Professor {prof_id} (stub)\n")

        # --- BACK ---
        elif choice == '5':
            return "main"
        


##
##TODO: CREATE OWN CLASS
##
def student_menu():
    while choice not in ['1', '2', '3', '4', '5']:
        print("Student Management")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: (1/2/3/4/5) ")
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice, please try again.")
    return choice






