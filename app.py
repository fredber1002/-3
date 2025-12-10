class Person:
    def __init__(self, name, id, email):
        self.name = name
        self.id = id
        self.email = email

    def get_role(self):
        pass

class Student(Person):
    def __init__(self, name, id, email):
        super().__init__(name, id, email)
        self.courses = []
        self.grades = {}

    def enroll(self, course):
        self.courses.append(course)

    def get_gpa(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

    def get_role(self):
        return "Student"

class Professor(Person):
    def __init__(self, name, id, email, department):
        super().__init__(name, id, email)
        self.department = department
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)
        course.professor = self

    def get_role(self):
        return "Professor"

class Course:
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits
        self.professor = None
        self.students = []
        self.grades = {}

    def add_student(self, student):
        self.students.append(student)
        student.enroll(self)

    def record_grade(self, student, grade):
        self.grades[student.id] = grade
        student.grades[self.code] = grade

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

class University:
    def __init__(self):
        self.students = []
        self.professors = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_professor(self, professor):
        self.professors.append(professor)

    def create_course(self, course):
        self.courses.append(course)

    def generate_report(self):
        print("Отчёт университета:")
        for course in self.courses:
            avg = course.get_average_grade()
            print(f"{course.code}: {course.name}, Средний балл: {avg}")

university = University()

student1 = Student("Анна Смирнова", "S001", "anna@edu.ru")
prof1 = Professor("Дмитрий Волков", "P001", "volkov@edu.ru", "Информатика")
course1 = Course("CS101", "Программирование на Python", 3)

university.add_student(student1)
university.add_professor(prof1)
university.create_course(course1)

course1.add_student(student1)
prof1.assign_course(course1)
course1.record_grade(student1, 4.5)

university.generate_report()

