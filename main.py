# импорт созданных классов
from class_mentor import Mentor         # импорт класса преподавателя
from class_student import Student       # импорт класса студента
from class_lecturer import Lecturer     # импорт класса лектора
from class_reviewer import Reviewer     # импорт класса проверяющего преподавателя


first_mentor = Lecturer("Gandalf", "Gray")
second_mentor = Reviewer("Gandalf", "White")

first_student = Student("Gimli", "Tolkien", "Dwarf")
second_student = Student("Legolas", "Tolkien", "Elves")
third_student = Student("Aragorn", "Tolkien", "Man")

first_student.courses_in_progress += ["Erebor"]
second_student.courses_in_progress += ["Mirkwood"]
second_mentor.courses_attached += ["Erebor"]

second_mentor.rate_hw(first_student, "Erebor", 10)



first_mentor.courses_attached += ["Erebor"]

first_student.rate_lecturer(first_mentor, "Erebor", 8)
second_student.rate_lecturer(first_mentor, "Erebor", 5)


print(first_student)
print(second_mentor)
print(first_mentor)