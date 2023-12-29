from class_student import Student
from class_lecturer import Lecturer

# метод для подсчета средней оценки за домашние задания
# по всем студентам в рамках конкретного курса
def determine_average_marks_of_students_for_course(
        students_list = [], course_name = str()):
    sum_of_marks = float(0.0)
    number_of_marks = int(0)

    for student in students_list:
        if course_name in student.grades.keys():
            for mark in student.grades[course_name]:
                sum_of_marks += mark
                number_of_marks += 1

    if sum_of_marks == 0:
        return 0.0

    return sum_of_marks/number_of_marks

# метод для подсчета средней оценки за лекции
# всех лекторов в рамках курса
def determine_average_marks_of_lecturers_for_course(
        lecturers_list = [], course_name = str()):
    sum_of_marks = float(0.0)
    number_of_marks = int(0)

    for lecturer in lecturers_list:
        if course_name in lecturer.grades.keys():
            for mark in lecturer.grades[course_name]:
                sum_of_marks += mark
                number_of_marks += 1

    if sum_of_marks == 0:
        return 0.0

    return sum_of_marks / number_of_marks