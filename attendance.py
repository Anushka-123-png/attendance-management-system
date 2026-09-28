from database import save_students
def mark_attendance(students):
    if not students:
        print("No students found.")
        return

    roll_no = input("Enter roll number: ")

    for student in students:
        if student["roll_no"] == roll_no:
            status = input("Enter attendance (P/A): ").upper()

        if status == "P":
            student["attendance"] = "Present"
            save_students(students)
            print("Attendance marked as Present.")

        elif status == "A":
            student["attendance"] = "Absent"
            save_students(students)
            print("Attendance marked as Absent.")

        else:
            print("Invalid attendance status.")

            return

    print("Student not found.")


def view_attendance(students):
    if not students:
        print("No students found.")
        return

    print("\nAttendance:")

    for student in students:
        attendance = student.get("attendance", "Not Marked")

        print(
            "Roll No:", student["roll_no"],
            "| Name:", student["name"],
            "| Attendance:", attendance
        )