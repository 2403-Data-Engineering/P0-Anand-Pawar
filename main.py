from presentation_layer.main_menu import main_menu
from presentation_layer.professor_menu import professor_menu
from presentation_layer.student_menu import student_menu
from presentation_layer.course_menu import course_menu
from presentation_layer.enrollment_menu import enrollment_menu

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
                current_menu = "course"
            elif choice == "4":
                current_menu = "enroll"
            elif choice == "5":
                current_menu = "exit"
            else:
                print("Invalid choice")
                current_menu = "main"

        elif current_menu == "professor":
            current_menu = professor_menu()

        elif current_menu == "student":
            current_menu = student_menu()

        elif current_menu == "course":
            current_menu = course_menu()

        elif current_menu == "enroll":
            current_menu = enrollment_menu()

    print("Exiting system...")


if __name__ == "__main__":
    run_app()