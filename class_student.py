from class_lecturer import Lecturer

class Student:
    """Класс, описывающий студентов"""
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    # перегрузка магического метода __str__
    def __str__(self):
        return (
                f"Имя: {self.name}\n"+
                f"Фамилия: {self.surname}\n"+
                f"Средняя оценка за домашние задания: {self.get_average_mark_for_homework()}\n" +
                f"Курсы в процессе изучения: {self.get_info_about_courses_on_progress()}\n" +
                f"Завершенные курсы: {self.get_info_about_finished_courses()}"
                )

    # метод для вычисления средней оценки студента
    def get_average_mark_for_homework(self):

        sum_of_marks = float(0.0)
        number_of_marks = int(0)

        if len(self.grades.keys()) == 0:
            return 0.0

        for key, values in self.grades.items():
            for value in values:
                sum_of_marks += value
                number_of_marks += 1

        return float(sum_of_marks / number_of_marks)


    # метод выставления оценок лекторам
    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Error"

    # метод для вывода курсов в процессе изучения
    def get_info_about_courses_on_progress(self):
        output_str = str("")
        if len(self.courses_in_progress) == 0:
            return "Курсы в процессе изучения отсутствуют"
        for i in range(len(self.courses_in_progress)):
            if i == 0:
                output_str += f"{self.courses_in_progress[i]}"
            elif i == (len(self.courses_in_progress) - 1):
                output_str += f", {self.courses_in_progress[i]}"
            else:
                output_str += f", {self.courses_in_progress[i]}"
        return output_str

    # метод для вывода завершенных списков
    def get_info_about_finished_courses(self):
        output_str = str("")
        if len(self.finished_courses) == 0:
            return "Завершенные курсы отсутствуют"
        for i in range(len(self.finished_courses)):
            if i == 0:
                output_str += f"{self.finished_courses[i]}"
            elif i == (len(self.finished_courses) - 1):
                output_str += f", {self.finished_courses[i]}"
            else:
                output_str += f", {self.finished_courses[i]}"
        return output_str