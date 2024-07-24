from models.student import Student
from models.course import Course
from utils.data_manager import save_students, load_students, save_courses, load_courses

class GradeBook:
    def __init__(self):
        self.student_list = load_students()
        self.course_list = load_courses()

    def add_student(self, email, names):
        student = Student(email, names)
        self.student_list.append(student)
        save_students(self.student_list)
        print(f"Added student: {email}, {names}")

    def add_course(self, name, trimester, credits):
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        save_courses(self.course_list)
        print(f"Added course: {name}, {trimester}, {credits}")

    def register_student_for_course(self, email, course_name, grade):
        student = next((s for s in self.student_list if s.email == email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)
        if student and course:
            student.register_for_course(course, grade)
            save_students(self.student_list)
            print(f"Registered student {email} for course {course_name} with grade {grade}")
        else:
            print(f"Student or course not found. Registration failed.")

    def calculate_ranking(self):
        # Ensure that GPA is up-to-date for all students
        for student in self.student_list:
            student.calculate_GPA()
        # Sort students based on GPA in descending order
        self.student_list.sort(key=lambda s: s.GPA, reverse=True)
        print("Calculated student ranking")
        return self.student_list

    def search_by_grade(self, grade):
        results = [student for student in self.student_list if any(c['grade'] == grade for c in student.courses_registered)]
        print(f"Found {len(results)} students with grade {grade}")
        return results

    def generate_transcript(self, email):
        student = next((s for s in self.student_list if s.email == email), None)
        if student:
            transcript = {
                'email': student.email,
                'names': student.names,
                'GPA': student.GPA,
                'courses_registered': student.courses_registered
            }
            print(f"Generated transcript for student {email}")
            return transcript
        print(f"No transcript found for student {email}")
        return None
