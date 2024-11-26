'''
class Student:
    count = 0
    # Constructor
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.courses = []  # List to store enrolled courses
        Student.count += 1

    # Methods to change attributes
    def change_age(self, age):
        self.age = age

    def change_name(self, name):
        self.name = name

    def change_gender(self, gender):
        self.gender = gender

    # Method to add a course to the student's course list
    def enroll_in_course(self, course):
        self.courses.append(course)
        print(f"{self.name} enrolled in {course.name}")

    # Method to remove a course from the student's course list
    def drop_course(self, course):
        self.courses.remove(course)
        print(f"{self.name} dropped {course.name}")

    # String representation of the object
    def __str__(self):
        courses_names = ", ".join([course.name for course in self.courses]) or "No courses"
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Enrolled in: {courses_names}"

# Course class definition
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(f"{student.name} added to {self.name}")

    def remove_student(self, student):
        self.students.remove(student)
        print(f"{student.name} removed from {self.name}")

    def __str__(self):
        students_names = ", ".join([student.name for student in self.students])
        return f"Course Name: {self.name}, Students: {students_names}"

# Creating instances of Student
student1 = Student("Rachel", 20, "female")
student2 = Student("Ross", 21, "male")
student3 = Student("Monica", 21, "female")

# Creating instances of Course
course1 = Course("Math")
course2 = Course("Computer Science")

# Adding courses to students
student1.enroll_in_course(course1)
student1.enroll_in_course(course2)

student2.enroll_in_course(course1)
student2.enroll_in_course(course2)

student3.enroll_in_course(course1)

# Printing details of students with their enrolled courses
print("student1 Details:")
print(student1)

print("student2 Details:")
print(student2)

# Removing a course
student1.drop_course(course1)
# Checking the details after dropping a course
print("student1 Details after and dropping Math:")
print(student1)
'''

from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/sum')
def calculate_sum():
    args = request.args
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    total_sum = number1+number2
    total_sum = number1 + number2

    response = {
        "number1": number1,
        "number2": number2,
        "total_sum": total_sum
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)
'''
from flask import Flask
'''
app = Flask(__name__)
@app.route('/echo/<text>')
def echo(text):
    response = {
        "echo" : text + " " + text
    }
    return response

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)






