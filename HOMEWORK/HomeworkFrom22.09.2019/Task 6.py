"""В классе Square определите метод change_size, позволяющий передавать ему число,
которое увеличивает или уменьшает (если оно отрицательное) каждую сторону объекта
Square на соответствующее значение."""


class ClsSquare:
    def __init__(self, size):
        self.size_a = size
        self.size_b = size
        self.size_c = size
        self.size_d = size
    
    def change_size(self, num):
        self.size_a = self.size_a + num
        self.size_b = self.size_b + num
        self.size_c = self.size_c + num
        self.size_d = self.size_d + num


tmpSquare1 = ClsSquare(25)
print(tmpSquare1.size_a, end = ' ')
print(tmpSquare1.size_b, end = ' ')
print(tmpSquare1.size_c, end = ' ')
print(tmpSquare1.size_d)
tmpSquare1.change_size(12)
print(tmpSquare1.size_a, end = ' ')
print(tmpSquare1.size_b, end = ' ')
print(tmpSquare1.size_c, end = ' ')
print(tmpSquare1.size_d)
tmpSquare1.change_size(-28)
print(tmpSquare1.size_a, end = ' ')
print(tmpSquare1.size_b, end = ' ')
print(tmpSquare1.size_c, end = ' ')
print(tmpSquare1.size_d)
