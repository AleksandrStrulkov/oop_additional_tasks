"""
Создай класс Bottle (бутылка) c полями

- Цвет (color) - строка
- Объем (volume) - число с плавающей точкой

Создай три экземпляра

- Красную 0.7
- Белую 0.3
- Черную 1.0
"""


class Bottle:

    def __init__(self, color, volume):
        self.color = color
        self.volume = volume

    @property
    def get(self):
        if type(self.volume) == str: raise

try:
    bottle_1 = Bottle("Красная", 2.0)
    bottle_2 = Bottle("Белая", 4)
    bottle_3 = Bottle("Синяя", 3.0)
    bottle_1.get
    bottle_2.get
    bottle_3.get
except:
    print(f"Введено строковое значение,\n\
измените на цифровое значение\n\
в одном из экземпляров класса ")
else:
    print(f"Отработано штатно!\n\
    {bottle_1.color} краска, {bottle_1.volume} кг.\n\
    {bottle_2.color} краска, {bottle_2.volume} кг.\n\
    {bottle_3.color} краска, {bottle_3.volume} кг.")
