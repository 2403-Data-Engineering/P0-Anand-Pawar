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