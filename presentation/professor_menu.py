from services import professor_service

def professor_menu():
    while True:
        print("Professor Management")
        print("1. Add Professor")
        print("2. View Professors")
        print("3. Update Professor")
        print("4. Delete Professor")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: (1/2/3/4/5)")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice, please try again.")
            continue
        
        elif choice == '1':
            first = input("First Name: ")
            last = input("Last Name: ")
            dept = input("Department: ")
            prof = professor_service.add_professor(first, last, dept)
            print(f"\nProfessor {prof.first_name} {prof.last_name} added successfully!\n")
            print(prof)

        elif choice == '2':
            print("\n--- Professors List ---")
            professors = professor_service.get_all_professors()
            for p in professors:
                print(f"{p['id']}. {p['name']}")
            prof_id = input("\nEnter Professor ID for a Report (or 'b' to go back): ")
            if prof_id.lower() == 'b':
                continue

            prof = professor_service.get_professor_by_id(prof_id)
            if not prof:
                print("Invalid ID")
                continue

            print(f"\nGenerating report for {prof.first_name} {prof.last_name}...\n")

        elif choice == '3':
            prof_id = input("Enter Professor ID to update: ")
            print("Enter Updates, match previous values to keep the same...")
            first = input("Updated First Name: ")
            last = input("Updated Last Name: ")
            dept = input("Updated Department: ")

            prof = professor_service.update_professor()
            if prof != None:
                print(f"Updating Professor {prof.id} (stub)\n")

        elif choice == '4':
            prof_id = input("Enter Professor ID to delete: ")
            professor_service.delete_professor(prof_id)

        elif choice == '5':
            return "main"