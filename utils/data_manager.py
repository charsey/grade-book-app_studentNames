import json
from models.student import Student
from models.course import Course

STUDENT_FILE = 'students.json'
COURSE_FILE = 'courses.json'

def save_students(students):
    data = [{
        'email': student.email,
        'names': student.names,
        'courses_registered': [{'course': {'name': cr['course']['name'], 'trimester': cr['course']['trimester'], 'credits': cr['course']['credits']}, 'grade': cr['grade']} for cr in student.courses_registered],
        'GPA': student.GPA
    } for student in students]

    with open(STUDENT_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def load_students():
    try:
        with open(STUDENT_FILE, 'r') as file:
            data = json.load(file)
            students = []
            for student_data in data:
                student = Student(
                    email=student_data['email'],
                    names=student_data['names'],
                    courses_registered=student_data['courses_registered'],
                    GPA=student_data['GPA']
                )
                students.append(student)
            return students
    except FileNotFoundError:
        return []

def save_courses(courses):
    data = [{'name': course.name, 'trimester': course.trimester, 'credits': course.credits} for course in courses]

    with open(COURSE_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def load_courses():
    try:
        with open(COURSE_FILE, 'r') as file:
            data = json.load(file)
            courses = []
            for course_data in data:
                course = Course(
                    name=course_data['name'],
                    trimester=course_data['trimester'],
                    credits=course_data['credits']
                )
                courses.append(course)
            return courses
    except FileNotFoundError:
        return []
