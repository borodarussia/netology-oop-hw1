class Student:
    """Класс, описывающий студентов"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # Метод выставления оценок лекторам
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"


class Mentor:
    """Родительский класс, описывающий преподавателей"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Преподаватель - лектор"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    """Преподаватель - эксперт, проверяющий домашние задания"""
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Error"


first_mentor = Lecturer("Gandalf", "Gray")
second_mentor = Reviewer("Gandalf", "White")
# print(f"Имя лектора: {lect1.name}\nФамилия лектора: {lect1.surname}\n\n***\n\n")

first_student = Student("Gimli", "Tolkien", "Dwarf")
second_student = Student("Legolas", "Tolkien", "Elves")
third_student = Student("Aragorn", "Tolkien", "Man")

first_student.courses_in_progress += ["Erebor"]
second_student.courses_in_progress += ["Mirkwood"]
second_mentor.courses_attached += ["Erebor"]

second_mentor.rate_hw(first_student, "Erebor", 10)

print(first_student.grades)

first_mentor.courses_attached += ["Erebor"]

first_student.rate_lecturer(first_mentor, "Erebor", 8)
second_student.rate_lecturer(first_mentor, "Erebor", 5)

print(first_mentor.grades)
