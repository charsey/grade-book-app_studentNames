from models.grade_book import GradeBook

def main():
    grade_book = GradeBook()

    while True:
        print("\nGrade Book Application")
        print("1. Add student")
        print("2. Add course")
        print("3. Register student for a course")
        print("4. Calculate and display ranking")
        print("5. Search students by grade")
        print("6. Generate transcript")
        print("7. Exit")

        choice = input("Choose an action: ")

        if choice == '1':
            email = input("Enter student's email: ")
            names = input("Enter student's names: ")
            grade_book.add_student(email, names)
        elif choice == '2':
            name = input("Enter course name: ")
            trimester = input("Enter trimester: ")
            credits = int(input("Enter credits: "))
            grade_book.add_course(name, trimester, credits)
        elif choice == '3':
            email = input("Enter student's email: ")
            course_name = input("Enter course name: ")
            grade = float(input("Enter grade: "))
            grade_book.register_student_for_course(email, course_name, grade)
        elif choice == '4':
            ranking = grade_book.calculate_ranking()
            print("\nStudent Ranking:")
            for idx, student in enumerate(ranking, start=1):
                print(f"{idx}. {student.names}, GPA: {student.GPA}")
        elif choice == '5':
            grade = float(input("Enter grade to search: "))
            results = grade_book.search_by_grade(grade)
            print(f"\nStudents with grade {grade}:")
            for student in results:
                print(f"{student.names}, Email: {student.email}")
        elif choice == '6':
            email = input("Enter student's email: ")
            transcript = grade_book.generate_transcript(email)
            if transcript:
                print(f"\nTranscript for {email}:")
                print(f"Names: {transcript['names']}")
                print(f"GPA: {transcript['GPA']}")
                print("Courses Registered:")
                for course in transcript['courses_registered']:
                    print(f"Course: {course['course']['name']}, Grade: {course['grade']}")
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
