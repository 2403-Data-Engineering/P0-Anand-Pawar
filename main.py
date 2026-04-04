from presentation.main_menu import main_menu
from presentation.professor_menu import professor_menu
from presentation.student_menu import student_menu

def run_app():
    current_menu = "main"

    while current_menu != "exit":

        if current_menu == "main":
            choice = main_menu()

            if choice == "1":
                current_menu = "professor"
            elif choice == "2":
                current_menu = "student"
            elif choice == "3":
                print("Courses not implemented yet")
                current_menu = "main"
            elif choice == "4":
                print("Enrollments not implemented yet")
                current_menu = "main"
            elif choice == "5":
                current_menu = "exit"
            else:
                print("Invalid choice")
                current_menu = "main"

        elif current_menu == "professor":
            current_menu = professor_menu()

        elif current_menu == "student":
            current_menu = student_menu()

    print("Exiting system...")


if __name__ == "__main__":
    run_app()