class Mentor:
    """Родительский класс, описывающий преподавателей"""
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []