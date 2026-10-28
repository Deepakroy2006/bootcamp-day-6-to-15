
class Student:

    total_students = 0

    def __init__(self, student_id, student_name, student_age):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age

        Student.total_students += 1

    def display(self):
        print("ID:", self.student_id)
        print("Name:", self.student_name)
        print("Age:", self.student_age)

    @classmethod
    def show_total_students(cls):
        print("Total Students:", cls.total_students)

    @staticmethod
    def is_adult(age):
        return age >= 18



class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("Name:", self.name)




class Teacher(Person):

    def __init__(self, teacher_id, teacher_name, subject):
        super().__init__(teacher_name)

        self.teacher_id = teacher_id
        self.subject = subject

    def display(self):
        print("Teacher ID:", self.teacher_id)
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)



class Course:

    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def assign_teacher(self, teacher):
        self.teacher = teacher

    def display(self):

        print("\nCourse:", self.course_name)

        if self.teacher:
            print("Teacher:", self.teacher.name)
        else:
            print("Teacher: Not Assigned")

        if len(self.students) == 0:
            print("Students: No students enrolled.")
            return

        print("Students:")

        for student in self.students:
            print(
                "-",
                student.student_id,
                student.student_name
            )



class Department:

    def __init__(self, department_name):
        self.department_name = department_name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display(self):

        print("\nDepartment:", self.department_name)

        if len(self.courses) == 0:
            print("No courses available.")
            return

        for course in self.courses:
            course.display()



class StudentManagementSystem:

    def __init__(self):
        self.students = []
        self.courses = []
        self.departments = []
        self.teachers = []

    # Add Student
    def add_student(self):

        try:
            student_id = int(input("Enter Student ID: "))

            for student in self.students:
                if student.student_id == student_id:
                    print("Student ID already exists.")
                    return

            student_name = input("Enter Student Name: ").strip()

            if student_name == "":
                print("Name cannot be empty.")
                return

            student_age = int(input("Enter Student Age: "))

            if student_age <= 0:
                print("Age must be greater than 0.")
                return

            student = Student(
                student_id,
                student_name,
                student_age
            )

            self.students.append(student)

            print("Student added successfully.")

        except ValueError:
            print("Please enter valid information.")

    
    def view_students(self):

        if len(self.students) == 0:
            print("No students available.")
            return

        print("\n--- All Students ---")

        for student in self.students:
            student.display()

    
    def search_student(self):

        student_name = input(
            "Enter student name to search: "
        ).strip().lower()

        for student in self.students:

            if student.student_name.lower() == student_name:

                print("\nStudent Found")
                student.display()
                return

        print("Student not found.")

    
    def update_student(self):

        try:
            student_id = int(
                input("Enter Student ID to update: ")
            )

            for student in self.students:

                if student.student_id == student_id:

                    new_name = input(
                        "Enter new name: "
                    ).strip()

                    new_age = int(
                        input("Enter new age: ")
                    )

                    if new_name == "" or new_age <= 0:
                        print("Invalid information.")
                        return

                    student.student_name = new_name
                    student.student_age = new_age

                    print("Student updated successfully.")
                    return

            print("Student not found.")

        except ValueError:
            print("Please enter valid information.")

    
    def delete_student(self):

        try:
            student_id = int(
                input("Enter Student ID to delete: ")
            )

            for student in self.students:

                if student.student_id == student_id:

                    self.students.remove(student)

                    # Remove student from courses
                    for course in self.courses:
                        if student in course.students:
                            course.students.remove(student)

                    print("Student deleted successfully.")
                    return

            print("Student not found.")

        except ValueError:
            print("Please enter a valid Student ID.")

    
    def show_student_details(self):

        try:
            student_id = int(
                input("Enter Student ID: ")
            )

            for student in self.students:

                if student.student_id == student_id:

                    print("\n--- Student Details ---")
                    student.display()

                    if Student.is_adult(student.student_age):
                        print("Status: Adult")
                    else:
                        print("Status: Minor")

                    return

            print("Student not found.")

        except ValueError:
            print("Please enter a valid Student ID.")


    def add_course(self):

        course_name = input(
            "Enter Course Name: "
        ).strip()

        if course_name == "":
            print("Course name cannot be empty.")
            return

        department_name = input(
            "Enter Department Name: "
        ).strip()

        if department_name == "":
            print("Department name cannot be empty.")
            return

        course = Course(course_name)

       
        for department in self.departments:

            if department.department_name.lower() == department_name.lower():

                department.add_course(course)
                self.courses.append(course)

                print("Course added to existing department.")
                return

        
        department = Department(department_name)

        department.add_course(course)

        self.departments.append(department)
        self.courses.append(course)

        print("Department and course added successfully.")

    
    def enroll_student(self):

        try:
            student_id = int(
                input("Enter Student ID: ")
            )

            selected_student = None

            for student in self.students:

                if student.student_id == student_id:
                    selected_student = student
                    break

            if selected_student is None:
                print("Student not found.")
                return

            course_name = input(
                "Enter Course Name: "
            ).strip()

            for course in self.courses:

                if course.course_name.lower() == course_name.lower():

                    if selected_student in course.students:
                        print("Student is already enrolled.")
                        return

                    course.add_student(selected_student)

                    print("Student enrolled successfully.")
                    return

            print("Course not found.")

        except ValueError:
            print("Please enter a valid Student ID.")

    
    def add_teacher(self):

        try:
            teacher_id = int(
                input("Enter Teacher ID: ")
            )

            teacher_name = input(
                "Enter Teacher Name: "
            ).strip()

            subject = input(
                "Enter Subject: "
            ).strip()

            if teacher_name == "" or subject == "":
                print("Teacher name and subject cannot be empty.")
                return

            teacher = Teacher(
                teacher_id,
                teacher_name,
                subject
            )

            self.teachers.append(teacher)

            print("Teacher added successfully.")

        except ValueError:
            print("Please enter a valid Teacher ID.")

    
    def assign_teacher(self):

        try:
            teacher_id = int(
                input("Enter Teacher ID: ")
            )

            selected_teacher = None

            for teacher in self.teachers:

                if teacher.teacher_id == teacher_id:
                    selected_teacher = teacher
                    break

            if selected_teacher is None:
                print("Teacher not found.")
                return

            course_name = input(
                "Enter Course Name: "
            ).strip()

            for course in self.courses:

                if course.course_name.lower() == course_name.lower():

                    course.assign_teacher(selected_teacher)

                    print("Teacher assigned successfully.")
                    return

            print("Course not found.")

        except ValueError:
            print("Please enter a valid Teacher ID.")

    
    def display_departments(self):

        if len(self.departments) == 0:
            print("No departments available.")
            return

        for department in self.departments:
            department.display()

    
    def run(self):

        while True:

            print("\n================================")
            print("   STUDENT MANAGEMENT SYSTEM")
            print("================================")

            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Update Student")
            print("5. Delete Student")
            print("6. Student Details")
            print("7. Add Course")
            print("8. Enroll Student")
            print("9. Add Teacher")
            print("10. Assign Teacher")
            print("11. Display Departments")
            print("12. Show Total Students")
            print("13. Exit")

            try:
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    self.add_student()

                elif choice == 2:
                    self.view_students()

                elif choice == 3:
                    self.search_student()

                elif choice == 4:
                    self.update_student()

                elif choice == 5:
                    self.delete_student()

                elif choice == 6:
                    self.show_student_details()

                elif choice == 7:
                    self.add_course()

                elif choice == 8:
                    self.enroll_student()

                elif choice == 9:
                    self.add_teacher()

                elif choice == 10:
                    self.assign_teacher()

                elif choice == 11:
                    self.display_departments()

                elif choice == 12:
                    Student.show_total_students()

                elif choice == 13:
                    print("Thank you for using the system.")
                    break

                else:
                    print("Please choose between 1 and 13.")

            except ValueError:
                print("Please enter a number.")



system = StudentManagementSystem()


system.run()