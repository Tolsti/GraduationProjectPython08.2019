"""Есть класс Person, конструктор которого принимает три параметра (не учитывая self)
– имя, фамилию и квалификацию специалиста.
Квалификация имеет значение заданное по умолчанию, равное единице."""
'''У класса Person есть метод, который возвращает строку, включающую в себя всю информацию о сотруднике.'''


class ClsPerson:
    qualification = 1
    
    def __init__(self, name, surname, qualification):
        self.name = name
        self.surname = surname
        self.qualification = qualification
    
    def showWorker(self):
        print('Карточка сотрудника: ', end = '')
        print('Имя: ' + self.name)
        print('\t\t\t\t\t Фамилия: ' + self.surname)
        print('\t\t\t\t\t Клалификация: ' + str(self.qualification))


tmpPerson1 = ClsPerson('Никита', 'Сидоренков', 3)
tmpPerson2 = ClsPerson('Александр', 'Смоляков', 2)
tmpPerson1.showWorker()
tmpPerson2.showWorker()
