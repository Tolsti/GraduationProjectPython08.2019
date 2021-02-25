"""Определите класс Apple с четырьмя переменными экземпляра,
представляющими четыре свойства яблока."""


class ClsApple:
    def __init__(self, weight, color, radius, taste):
        self.weight = weight
        self.color = color
        self.radius = radius
        self.taste = taste


tmpApple = ClsApple(24, 'green', 5, 'sour')
print(tmpApple.weight)
print(tmpApple.color)
print(tmpApple.radius)
print(tmpApple.taste)
