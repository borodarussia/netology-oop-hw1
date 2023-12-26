from class_mentor import Mentor

class Lecturer(Mentor):
    """Преподаватель - лектор"""
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return(f"Имя: {self.name}\n" +
               f"Фамилия: {self.surname}\n" +
               f"Средняя оценка за лекции: {self.get_average_mark_for_lecture()}")
    # метод для определения средней оценки за проведенные лекции
    def get_average_mark_for_lecture(self):

        sum_of_marks = float(0.0)
        number_of_marks = int(0)

        if len(self.grades.keys()) == 0:
            return 0.0

        for key, values in self.grades.items():
            for value in values:
                sum_of_marks += value
                number_of_marks += 1

        return float(sum_of_marks / number_of_marks)