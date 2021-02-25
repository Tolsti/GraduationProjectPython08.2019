"""Создайте классы Rectangle и Square с методом calculate_perimeter,
вычисляющим периметр фигур, которые эти классы представляют.
Создайте объекты Rectangle и Square вызовите в них этот метод."""


class ClsRectangle:
    def __init__(self, size_a, size_b):
        self.a = size_a
        self.b = size_b
    
    def calculate_perimeter(self):
        return 2 * (self.a + self.b)


class ClsSquare:
    def __init__(self, size_a):
        self.a = size_a
    
    def calculate_perimeter(self):
        return 4 * self.a


tmpRectangle1 = ClsRectangle(5, 12)
tmpSquare1 = ClsSquare(7)
print('Периметр прямоугольника: ' + str(tmpRectangle1.calculate_perimeter()))
print('Периметр квадрата: ' + str(tmpSquare1.calculate_perimeter()))
