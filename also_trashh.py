


    def add_course(self, course_name: str) -> None:
        """Add a course to the student's schedule."""
        if course_name not in self.courses:
            self.courses.append(course_name)
            self.grades[course_name] = 0.0
    
    def update_grade(self, course_name: str, grade: float) -> bool:
        """Update the grade for a specific course."""
        if course_name in self.courses and 0 <= grade <= 100:
            self.grades[course_name] = grade
            return True
        return False
    
    def get_average_grade(self) -> float:
        """Calculate the average grade across all courses."""
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)
    
    def to_dict(self) -> Dict:
        """Convert student data to dictionary for JSON serialization."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "enrollment_date": self.enrollment_date,
            "courses": self.courses,
            "grades": self.grades
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Student':
        """Create a Student instance from dictionary data."""
        student = cls(data["student_id"], data["name"], data["age"], data["grade"])
        student.enrollment_date = data["enrollment_date"]
        student.courses = data["courses"]
        student.grades = data["grades"]
        return student
    
    def __str__(self) -> str:
        return f"Student: {self.name} (ID: {self.student_id}) - Grade: {self.grade}"


class StudentManager:
    """Manages a collection of students with CRUD operations."""
    
    def __init__(self, data_file: str = "students.json"):
        self.data_file = data_file
        self.students: Dict[str, Student] = {}
        self.load_data()
    
    def add_student(self, student: Student) -> bool:
        """Add a new student to the system."""
        if student.student_id in self.students:
            return False
        self.students[student.student_id] = student
        self.save_data()
        return True
    
    def get_student(self, student_id: str) -> Optional[Student]:
        """Retrieve a student by ID."""
        return self.students.get(student_id)
    
    def update_student(self, student_id: str, name: str = None, age: int = None, grade: str = None) -> bool:
        """Update student information."""
        student = self.get_student(student_id)
        if not student:
            return False
        if name:
            student.name = name
        if age:
            student.age = age
        if grade:
            student.grade = grade
        self.save_data()
        return True
    
    def delete_student(self, student_id: str) -> bool:
        """Remove a student from the system."""
        if student_id not in self.students:
            return False
        del self.students[student_id]
        self.save_data()
        return True
    
    def list_all_students(self) -> List[Student]:
        """Return a list of all students."""
        return list(self.students.values())
    
    def search_students(self, search_term: str) -> List[Student]:
        """Search students by name or ID (case-insensitive)."""
        search_term = search_term.lower()
        results = []
        for student in self.students.values():
            if search_term in student.name.lower() or search_term in student.student_id.lower():
                results.append(student)
        return results
    
    def get_students_by_grade(self, grade: str) -> List[Student]:
        """Filter students by their grade level."""
        return [s for s in self.students.values() if s.grade == grade]
    
    def save_data(self) -> None:
        """Save all student data to JSON file."""
        try:
            data = [student.to_dict() for student in self.students.values()]
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_data(self) -> None:
        """Load student data from JSON file."""
        if not os.path.exists(self.data_file):
            return
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
            for item in data:
                student = Student.from_dict(item)
                self.students[student.student_id] = student
        except Exception as e:
            print(f"Error loading data: {e}")


def main():
    """Main program loop with user interaction."""
    manager = StudentManager()
    
    while True:
        print("\n" + "="*50)
        print("STUDENT MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Course to Student")
        print("7. Update Student Grade")
        print("8. View Student Details")
        print("9. Exit")
        print("="*50)
        
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '1':
            # Add student
            student_id = input("Enter student ID: ").strip()
            if manager.get_student(student_id):
                print("Student ID already exists!")
                continue
            name = input("Enter student name: ").strip()
            age = int(input("Enter student age: "))
            grade = input("Enter student grade (e.g., 10th): ").strip()
            student = Student(student_id, name, age, grade)
            if manager.add_student(student):
                print(f"Student {name} added successfully!")
            else:
                print("Failed to add student.")
        
        elif choice == '2':
            # View all students
            students = manager.list_all_students()
            if not students:
                print("No students enrolled.")
            else:
                print(f"\nTotal Students: {len(students)}")
                for s in students:
                    print(f"  {s} - Courses: {len(s.courses)}")
        
        elif choice == '3':
            # Search students
            search = input("Enter name or ID to search: ").strip()
            results = manager.search_students(search)
            if results:
                print(f"\nFound {len(results)} student(s):")
                for s in results:
                    print(f"  {s}")
            else:
                print("No students found.")
        
        elif choice == '4':
            # Update student
            student_id = input("Enter student ID to update: ").strip()
            student = manager.get_student(student_id)
            if not student:
                print("Student not found.")
                continue
            name = input(f"Enter new name (current: {student.name}, press Enter to skip): ").strip()
            age_input = input(f"Enter new age (current: {student.age}, press Enter to skip): ").strip()
            age = int(age_input) if age_input else None
            grade = input(f"Enter new grade (current: {student.grade}, press Enter to skip): ").strip()
            if manager.update_student(student_id, name or None, age, grade or None):
                print("Student updated successfully!")
            else:
                print("Failed to update student.")
        
        elif choice == '5':
            # Delete student
            student_id = input("Enter student ID to delete: ").strip()
            confirm = input(f"Are you sure you want to delete student {student_id}? (y/n): ").strip().lower()
            if confirm == 'y' and manager.delete_student(student_id):
                print("Student deleted successfully!")
            else:
                print("Deletion cancelled or failed.")
        
        elif choice == '6':
            # Add course
            student_id = input("Enter student ID: ").strip()
            student = manager.get_student(student_id)
            if not student:
                print("Student not found.")
                continue
            course = input("Enter course name: ").strip()
            student.add_course(course)
            manager.save_data()
            print(f"Course '{course}' added to {student.name}'s schedule.")
        
        elif choice == '7':
            # Update grade
            student_id = input("Enter student ID: ").strip()
            student = manager.get_student(student_id)
            if not student:
                print("Student not found.")
                continue
            if not student.courses:
                print("Student is not enrolled in any courses.")
                continue
            print(f"Available courses: {', '.join(student.courses)}")
            course = input("Enter course name: ").strip()
            grade = float(input("Enter grade (0-100): "))
            if student.update_grade(course, grade):
                manager.save_data()
                print("Grade updated successfully!")
            else:
                print("Failed to update grade. Check course name and grade value.")
        
        elif choice == '8':
            # View student details
            student_id = input("Enter student ID: ").strip()
            student = manager.get_student(student_id)
            if not student:
                print("Student not found.")
                continue
            print("\n" + "="*50)
            print("STUDENT DETAILS")
            print("="*50)
            print(f"ID: {student.student_id}")
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Grade: {student.grade}")
            print(f"Enrollment Date: {student.enrollment_date}")
            print(f"Average Grade: {student.get_average_grade():.2f}")
            print("\nCourses and Grades:")
            for course, grade in student.grades.items():
                print(f"  {course}: {grade:.2f}%")
            print("="*50)
        
        elif choice == '9':
            print("Thank you for using the Student Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
