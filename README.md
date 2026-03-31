# P0 – College Administration System

## Overview

Build a Python console application that models a college course registration system. The system tracks **professors**, **classes**, and **students**, supporting the following relationships:

- **Professor → Classes:** One-to-many (a professor teaches multiple classes)
- **Student ↔ Classes:** Many-to-many (students enroll in multiple classes, classes have multiple students)

The application performs CRUD operations against a relational database and generates formatted reports as HTML and Markdown files.

---

## Technologies

- **Python**
- **MySQL**
- **mysql-connector-python** – database access via parameterized SQL
- **Yattag** and/or **mdutils** – report generation as HTML and/or Markdown (choose one or both)
- *Stretch:* **SQLAlchemy** – ORM as an alternative to raw SQL
- *Stretch:* **FastAPI** – REST API exposure

---

## Project Basics

### Console Interface

The application should not be written as a single linear script that runs top to bottom. Instead, build a **menu system** — a set of reusable menu screens that the user navigates through. Each menu should be able to display options, accept user input, invoke service methods based on that input, and navigate to other menus. Think of it as a simple screen-based UI: a main menu leads to sub-menus (e.g., "Manage Professors," "Manage Classes"), and each sub-menu provides the relevant CRUD operations before returning the user back.

### Architecture

The application should follow a **layered architecture** with three layers: a **presentation layer** (the console menus and all user-facing I/O), a **service layer** (business logic and orchestration), and a **data layer** (all direct database access). The presentation layer calls into the service layer, which in turn calls into the data layer. Menus should never import or call data layer code directly — if a menu needs data, it goes through a service method.

### Report Generation

Use **Yattag** (HTML) and/or **mdutils** (Markdown) to generate formatted report files. The reports don't need to be fancy — just clearly present the relevant data in a readable format and write it out to a file.

### Database

Every table must have a dedicated primary key column. Use foreign keys to enforce **referential integrity**, but do not use **cascade behavior** on deletes or updates — the application should handle these relationships explicitly. Deletes do not have to physically remove rows; you may use a soft-delete approach (e.g., an `active` flag or similar) instead.

---

- [ ] As an administrator, I can **add a new professor** to the system.
- [ ] As an administrator, I can **view all professors**.
- [ ] As an administrator, I can **update a professor's** information.
- [ ] As an administrator, I can **remove a professor** who is no longer teaching.
- [ ] As an administrator, I can **create a new class** and assign it to a professor.
- [ ] As an administrator, I can **view all classes**, including the assigned professor.
- [ ] As an administrator, I can **update a class's** details (e.g., reassign to a different professor).
- [ ] As an administrator, I can **delete a class** from the system.
- [ ] As an administrator, I can **add a new student** to the system.
- [ ] As an administrator, I can **view all students**.
- [ ] As an administrator, I can **update a student's** information.
- [ ] As an administrator, I can **remove a student** from the system.
- [ ] As an administrator, I can **enroll a student in a class**.
- [ ] As an administrator, I can **drop a student from a class**.
- [ ] As an administrator, I can **view all students enrolled in a given class**.
- [ ] As an administrator, I can **view all classes a given student is enrolled in**.
- [ ] As an administrator, I can **generate a student enrollment report** (as HTML or Markdown) for a selected student, listing all classes they are enrolled in.
- [ ] As an administrator, I can **generate a professor summary report** (as HTML or Markdown) for a selected professor, listing all classes they are teaching and the students enrolled in each.

---

## Functional Requirements

### Professors

- A professor has a name and department.
- The system prevents deleting a professor who is currently assigned to one or more classes.

### Classes

- A class has a name, subject/course code, and an assigned professor.
- A class cannot be created without assigning it to an existing professor.

### Students

- A student has a name and a major.
- The system prevents deleting a student who is currently enrolled in one or more classes.

### Enrollment

- A student can enroll in multiple classes; a class can have multiple students.
- The system prevents duplicate enrollments (same student in the same class twice).
- Dropping an enrollment removes only the association, not the student or the class.

### Reports

- A student enrollment report lists the student's name and all classes they are enrolled in, with professor and course code for each.
- A professor summary report lists the professor's name, all classes they teach, and the students enrolled in each class.
- Reports are generated as files (HTML via Yattag and/or Markdown via mdutils).

### Console Interface

- The application presents a menu-driven console interface for all operations.
- Invalid input is handled gracefully with meaningful error messages.

### Stretch – ORM

- Refactor the data access layer to use SQLAlchemy instead of raw SQL via mysql-connector-python.

### Stretch – REST API

- Expose all CRUD and enrollment operations as HTTP endpoints using FastAPI.
- Reports are available as downloadable endpoints.

---

## Deliverables

- **Source code** pushed to your GitHub project repository by end of business on the due date.
- **ERD** describing the database schema, included in the repository.
- **Live demonstration** of the working application during project presentations.
