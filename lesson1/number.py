"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:

    def __init__(self, value):
        self.value = value

    def get(self):
        return self.value

    def add(self, item):
        self.value += item
        return self.value


    def substract(self, item):
        self.value -= item
        if self.value <= 0: raise
        return self.value


try:
    n = Number(1)
    n.add(int(input()))
    n.substract(int(input()))
except:
    print("Это не может быть меньше или равно 0")
else:
    print(f"Все штатно отработано: остаток {n.get()}")
finally:
    print("Всем спасибо")
