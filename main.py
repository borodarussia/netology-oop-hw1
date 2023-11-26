class Student:
    """Класс, описывающий студентов"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    """Родительский класс, описывающий преподавателей"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    """Преподаватель - лектор"""
    pass


class Reviewer(Mentor):
    """Преподаватель - эксперт, проверяющий домашние задания"""
    pass