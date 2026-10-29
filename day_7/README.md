
## Day 7 – Python Object-Oriented Programming

An OOP-based Student Management CLI Application developed as part of the
Project Nexelis – Intern-to-Engineer Bootcamp.


## 1. Project Objective

The objective of Day 7 is to understand Object-Oriented Programming (OOP)
and learn how real-world entities can be represented as software objects.

The Day 6 Student Management application was converted into an
OOP-based application using classes, objects, constructors, attributes,
methods, encapsulation, inheritance, composition, class methods,
and static methods.


## 2. Practical Task

The application represents the following real-world entities as classes:

- Student
- Course
- Department
- Teacher

The application also uses a `StudentManagementSystem` class to manage
the overall application operations and menu.


## 3. OOP Concepts Covered

The project demonstrates the following Python OOP concepts:

- Classes
- Objects
- Constructors
- Attributes
- Methods
- Encapsulation
- Inheritance
- Composition
- Class Methods
- Static Methods


## 4. What is OOP?

Object-Oriented Programming is a programming approach where software is
designed using objects that represent real-world entities.

For example:

    Real World Entity       Software Representation

    Student                 Student Object
    Course                  Course Object
    Department              Department Object
    Teacher                 Teacher Object

OOP helps organize related data and behavior together and makes
applications easier to understand, maintain, and extend.



## 5. Class Structure

### Student

The `Student` class represents an individual student.

It stores:

- Student ID
- Student Name
- Student Age

It also provides a method to display student information.

Example:

python
class Student:

    def __init__(self, student_id, student_name, student_age):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age

    def display(self):
        print("Student ID:", self.student_id)
        print("Name:", self.student_name)
        print("Age:", self.student_age)

## 6 . StudentManagementSystem

The StudentManagementSystem class manages the overall application.

It handles:

Adding students
Viewing students
Searching students
Updating students
Deleting students
Adding courses
Enrolling students
Adding teachers
Assigning teachers
Displaying departments
Running the application menu

## 7. Class Relationships

The main relationship required by the Day 7 challenge is:

Department
     |
     | contains
     ↓
  Course
     |
     | contains
     ↓
  Student

A department can contain multiple courses, and a course can contain
multiple enrolled students.

A teacher can also be assigned to a course.

              Department
                  |
              contains
                  ↓
               Course
              /      \
        contains    assigned
           ↓           ↓
       Students      Teacher

## 8. Technologies Used
Technology	   Purpose
Python 3	   Application development
VS Code	Code    development and testing
Git	            Version control
GitHub	         Remote repository
Terminal	     Running and testing the CLI