from attendance import mark_attendance, view_attendance
from database import save_students, load_students

students = load_students()

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)
    save_students(students)

    print("Student added successfully!")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent List:")

    for student in students:
        print("Roll No:", student["roll_no"], "| Name:", student["name"])
while True:
    print("\n==============================")
    print("   ATTENDANCE MANAGEMENT SYSTEM")
    print("==============================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. View Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        mark_attendance(students)

    elif choice == "4":
        view_attendance(students)

    elif choice == "5":
        print("Thank you for using Attendance Management System!")
        break

    else:
        print("Invalid choice. Please try again.")