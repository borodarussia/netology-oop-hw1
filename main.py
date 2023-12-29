# импорт созданных классов
from class_mentor import Mentor         # импорт класса преподавателя
from class_student import Student       # импорт класса студента
from class_lecturer import Lecturer     # импорт класса лектора
from class_reviewer import Reviewer     # импорт класса проверяющего преподавателя

from methods_for_task_4 import determine_average_marks_of_students_for_course, determine_average_marks_of_lecturers_for_course


# объявление переменных
first_lecturer = Lecturer("Theoden", "Rohirrim")
second_lecturer = Lecturer("Denethor II", "Gondor")

first_reviewer = Reviewer("Gandalf", "Gray")
second_reviewer = Reviewer("Elrond", "Rivendell")

first_student = Student("Gimli", "Tolkien", "Dwarf")
second_student = Student("Legolas", "Tolkien", "Elves")
third_student = Student("Aragorn", "Tolkien", "Man")

# добавление курсов в прогрессе у студентов
first_student.courses_in_progress += ["Erebor"]
first_student.courses_in_progress += ["Mordor"]

second_student.courses_in_progress += ["Mordor"]
second_student.courses_in_progress += ["Gondolin"]

third_student.courses_in_progress += ["Erebor"]
third_student.courses_in_progress += ["Mordor"]
third_student.courses_in_progress += ["Shire"]
third_student.courses_in_progress += ["Gondolin"]

# добавление курсов лекторам
first_lecturer.courses_attached += ["Gondolin"]
first_lecturer.courses_attached += ["Shire"]

second_lecturer.courses_attached += ["Erebor"]
second_lecturer.courses_attached += ["Mordor"]

# добавление курсов проверяющим
first_reviewer.courses_attached += ["Erebor"]
first_reviewer.courses_attached += ["Mordor"]
first_reviewer.courses_attached += ["Shire"]
first_reviewer.courses_attached += ["Gondolin"]

second_reviewer.courses_attached += ["Erebor"]
second_reviewer.courses_attached += ["Mordor"]
second_reviewer.courses_attached += ["Shire"]
second_reviewer.courses_attached += ["Gondolin"]

# проставление оценок студентам
first_reviewer.rate_hw(third_student, "Erebor", 4)
second_reviewer.rate_hw(third_student, "Erebor", 7)
first_reviewer.rate_hw(second_student, "Mordor", 3)
second_reviewer.rate_hw(second_student, "Mordor", 6)
first_reviewer.rate_hw(first_student, "Erebor", 8)
second_reviewer.rate_hw(first_student, "Erebor", 1)

first_reviewer.rate_hw(third_student, "Mordor", 10)
second_reviewer.rate_hw(third_student, "Mordor", 3)
first_reviewer.rate_hw(second_student, "Gondolin", 6)
second_reviewer.rate_hw(second_student, "Gondolin", 3)
first_reviewer.rate_hw(first_student, "Mordor", 2)
second_reviewer.rate_hw(first_student, "Mordor", 6)

first_reviewer.rate_hw(third_student, "Shire", 3)
second_reviewer.rate_hw(third_student, "Mordor", 2)
first_reviewer.rate_hw(second_student, "Gondolin", 7)
second_reviewer.rate_hw(second_student, "Mordor", 9)
first_reviewer.rate_hw(first_student, "Mordor", 1)
second_reviewer.rate_hw(first_student, "Erebor", 5)

# проставление оценок преподавателям
first_student.rate_lecturer(second_lecturer, "Erebor", 10)
second_student.rate_lecturer(first_lecturer, "Gondolin", 3)
third_student.rate_lecturer(first_lecturer, "Shire", 5)

first_student.rate_lecturer(second_lecturer, "Mordor", 8)
second_student.rate_lecturer(second_lecturer, "Mordor", 1)
third_student.rate_lecturer(second_lecturer, "Erebor", 2)

first_student.rate_lecturer(second_lecturer, "Erebor", 3)
second_student.rate_lecturer(first_lecturer, "Gondolin", 4)
third_student.rate_lecturer(second_lecturer, "Mordor", 5)

# списки с оценками
students_list = [first_student, second_student, third_student] # список студентов
lecturers_list = [first_lecturer, second_lecturer] # список лекторов

# среднее значение оценок студентов за курсы
print("Оценка за курс \"Mordor\": ",
      '%.2f' % determine_average_marks_of_students_for_course(students_list = students_list,
                                                     course_name = "Mordor"))
print("Оценка за курс \"Gondolin\": ",
      '%.2f' % determine_average_marks_of_students_for_course(students_list = students_list,
                                                     course_name = "Gondolin"))
print("Оценка за курс \"Erebor\": ",
      '%.2f' % determine_average_marks_of_students_for_course(students_list = students_list,
                                                     course_name = "Erebor"))
print("Оценка за курс \"Shire\": ",
      '%.2f' % determine_average_marks_of_students_for_course(students_list = students_list,
                                                     course_name = "Shire"))

# среднее значение оценок лекторов за курсы
print("Оценка за курс \"Mordor\": ",
      '%.2f' % determine_average_marks_of_lecturers_for_course(lecturers_list = lecturers_list,
                                                     course_name = "Mordor"))
print("Оценка за курс \"Gondolin\": ",
      '%.2f' % determine_average_marks_of_lecturers_for_course(lecturers_list = lecturers_list,
                                                     course_name = "Gondolin"))
print("Оценка за курс \"Erebor\": ",
      '%.2f' % determine_average_marks_of_lecturers_for_course(lecturers_list = lecturers_list,
                                                     course_name = "Erebor"))
print("Оценка за курс \"Shire\": ",
      '%.2f' % determine_average_marks_of_lecturers_for_course(lecturers_list = lecturers_list,
                                                     course_name = "Shire"))

# вывод информации о студентах
print("\n\n\nИнформация о студентах:")
print(first_student)
print(second_student)
print(third_student)

print("\n\n\nИнформация о лекторах:")
print(first_lecturer)
print(second_lecturer)

print("\n\n\nИнформация о ревьюверах:")
print(first_reviewer)
print(second_reviewer)