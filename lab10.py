class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.marks = {}

    def add_mark(self, subject, mark):
        self.marks[subject] = mark

    def get_average_mark(self):
        if not self.marks:
            return 0
        total_marks = sum(self.marks.values())
        return total_marks / len(self.marks)

    def display_student_details(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")
        print(f"Average Mark: {self.get_average_mark()}")


students = {}

while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. Add Mark for a Student")
    print("3. Display Student Details")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        student = Student(student_id, name)
        students[student_id] = student
        print("Student added successfully!")

    elif choice == "2":
        student_id = input("Enter Student ID: ")
        if student_id in students:
            subject = input("Enter Subject: ")
            mark = float(input("Enter Mark: "))
            students[student_id].add_mark(subject, mark)
            print("Mark added successfully!")
        else:
            print("Student not found. Please add the student first.")

    elif choice == "3":
        student_id = input("Enter Student ID: ")
        if student_id in students:
            students[student_id].display_student_details()
        else:
            print("Student not found. Please add the student first.")

    elif choice == "4":
        break

    else:
        print("Invalid choice. Please try again.")
