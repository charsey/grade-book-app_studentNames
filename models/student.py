class Student:
    def __init__(self, email, names, courses_registered=None, GPA=0.0):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered if courses_registered else []
        self.GPA = GPA

    def register_for_course(self, course, grade):
        print(f"Registering course: {course.name}, Grade: {grade}")
        # Convert percentage grade to 4.0 scale
        gpa_grade = self.convert_to_gpa_scale(grade)
        print(f"Converted GPA Grade: {gpa_grade}")
        self.courses_registered.append({'course': {'name': course.name, 'trimester': course.trimester, 'credits': course.credits}, 'grade': gpa_grade})
        print(f"Registered courses: {self.courses_registered}")
        self.calculate_GPA()
        print(f"Calculated GPA: {self.GPA}")

    def convert_to_gpa_scale(self, percentage):
        if percentage >= 90:
            return 4.0
        elif percentage >= 80:
            return 3.0
        elif percentage >= 70:
            return 2.0
        elif percentage >= 60:
            return 1.0
        else:
            return 0.0

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
            print("No courses registered. GPA set to 0.0")
            return
        
        total_credits = sum(cr['course']['credits'] for cr in self.courses_registered)
        if total_credits == 0:
            self.GPA = 0.0
            print("Total credits are zero. GPA set to 0.0")
            return

        total_points = sum(cr['grade'] * cr['course']['credits'] for cr in self.courses_registered)
        print(f"Total points: {total_points}, Total credits: {total_credits}")
        self.GPA = total_points / total_credits
        print(f"New GPA: {self.GPA}")
