from class_mentor import Mentor
from class_student import Student

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
    # перегрузка магического метода __str__
    def __str__(self):
        return (f"Имя: {self.name}\n" +
                f"Фамилия: {self.surname}")