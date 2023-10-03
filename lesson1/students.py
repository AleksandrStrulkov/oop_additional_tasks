"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число

Создай два экземпляра

- Алиса , 3 [курс]
- Маргарита , 2 [курс]
"""


class Student:

    def __init__(self, name: str, course: int):
        self.name = name
        self.course = course

    @property
    def get(self):
        if type(self.name) == int: raise
        if type(self.course) == str: raise

try:
    student_1 = Student("Алиса", 3)
    student_2 = Student("Маргарита", 2)
    student_1.get
    student_2.get
except:
    print("Неправильно введены значения")
else:
    print(f"Программа отработала штатно:\n\
    {student_1.name, student_1.course}\n\
    {student_2.name, student_2.course}")

