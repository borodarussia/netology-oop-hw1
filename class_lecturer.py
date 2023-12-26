from class_mentor import Mentor

class Lecturer(Mentor):
    """Преподаватель - лектор"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}