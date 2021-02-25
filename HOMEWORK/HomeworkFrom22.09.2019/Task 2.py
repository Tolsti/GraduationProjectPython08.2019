"""Создайте класс Circle с методом area, подсчитывающим и возвращающим площадь круга.
Затем создайте объект Circle, вызовите в нем метод area и выведите результат.
Воспользуйтесь функцией pi из встроенного в Python модуля math."""

import math


class ClsCircle:
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return math.pi * self.radius ** 2


tmpC = ClsCircle(5)
print(tmpC.area())
