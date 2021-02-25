"""Создайте класс Triangle с методом area, подсчитывающим и возвращающим площадь треугольника.
Затем создайте объект Triangle, вызовите в нем area и выведите результат"""
import math


class ClsTriangle:
    def __init__(self, size_a, size_b, size_c):
        self.a = size_a
        self.b = size_b
        self.c = size_c
    
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


tmpTriangle1 = ClsTriangle(3, 5, 7)
print(tmpTriangle1.area())
