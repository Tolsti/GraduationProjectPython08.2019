import random

"""создать пустую функцию"""


def fun():
    pass


fun()

'''Написать функцию, которая принимает число,
возвращает его значение умноженное на два'''


def fun1(a):
    a = a * 2
    return a


print(fun1(5))

'''Напишем функцию, которая определяет параметр на чётность.
Если чётное число принтим (‘yes’) в ином случае (‘no’)'''


def fun2(a):
    if a % 2 == 0:
        print('yes')
    else:
        print('no')


fun2(4)

'''Пишем функцию, принимающую два аргумента.
После чего проверим, если первое число больше 10, принтим (‘да’).
Если меньше(‘нет’)'''

num1 = 12
num2 = 2


def fun3(a, b):
    if a > 10:
        print('да')
    else:
        print('нет')


fun3(num1, num2)

'''Написать лямбда функцию, которая делит по модулю(%) два аргумента'''

number = lambda num3, num4: num3 % num4
print(number(2, 4))

'''Создадим функцию с простыми командами. Обернём её в декоратор,
который бы дополнял возможности функции'''

# дополнил задание при вводе имени рамка растягивается на длину вводимой сторки(имени)
tmpName = input("Введите Ваше имя: ")


def countTab(a):  # функция считает длину строки и растягивает знар = на все имя
    tmpTab = '======'
    tmp = len(a)
    while tmp > 0:
        tmpTab = tmpTab + '='
        tmp -= 1
    return tmpTab


def decorator(fun4):
    def wrap():
        print("Привет!!!")
        print(countTab(tmpName))
        print("|| ", end='')
        fun4()
        print("||", end='')
        print("\n" + countTab(tmpName))

        print("|| ", end='')
        fun4()
        print("||", end='')
        print("\n" + countTab(tmpName))

    return wrap


@decorator
def fun4():
    print(tmpName, end=' ')
    print(tmpName, end=' ')


fun4()

'''Использовать функцию map и filter'''

numSquare = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def funSquare(a):
    return a ** 2


def funCheckEven(a):
    return a % 2 == 0


numSquare = list(map(funSquare, numSquare))
print(numSquare)
numSquare = list(filter(funCheckEven, numSquare))
print(numSquare)

'''Создадим чистую и нечистую функцию'''

radius = 34


def cleanFunction(r):  # чистая функция вычисляет площадь круга
    pi = 3.14
    return pi * r ** 2


def noCleanFunction():  # не чистая функция вычисляет площадь круга
    pi = 3.14
    s = pi * radius ** 2
    print("Площадь круга: " + str(s))


noCleanFunction()

print("Площадь круга: " + str(cleanFunction(radius)))

'''Сделать функцию поиска минимума и максимума в списке'''

arr = [random.randint(0, 100) for i in range(10)]
print(arr)


def funSearchMinMax(a):
    min = 10000
    max = -10000
    i = 0
    while i < len(a):
        if a[i] < min:
            min = a[i]
        if a[i] > max:
            max = a[i]
        i += 1
    print("Минимальный элемент: " + str(min))
    print("Максимальный элемент: " + str(max))


funSearchMinMax(arr)

'''Написать функцию, которая определяет,
является ли год високосным. Пользователь вводит год,
если он високосный, то функция возвращает True. Если нет, то False'''

yearInput = int(input("Введите год: "))


def funLeapYear(y):
    if y % 4 == 0:
        return True
    else:
        return False


print("Год высокосный: " + str(funLeapYear(yearInput)))

'''Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
и возвращающую время года, которому этот месяц принадлежит
(зима, весна, лето или осень)'''

monthInput = 0
while monthInput <= 0 or monthInput > 12:
    monthInput = int(input("Введите номер месяца: "))


def funMonthShow(a):
    if a >= 3 and a <= 5:
        print("Весна")
    elif a >= 6 and a <= 8:
        print("Лето")
    elif a >= 9 and a <= 11:
        print("Осень")
    else:
        print("Зима")


funMonthShow(monthInput)

'''Написать функцию date, принимающую 3 аргумента — день,
месяц и год. Вернуть True, если такая дата есть в нашем календаре,
и False иначе'''

arrMonth = {'январь': 31, 'февраль': 0, 'март': 31, 'апрель': 30,
            'май': 31, 'июнь': 30, 'июль': 31, 'август': 31,
            'сентябрь': 30, 'октябрь': 31, 'ноябрь': 30, 'декабрь': 31}
day = int(input("Введите день: "))

month = ''
flag = True
while flag:
    month = str(input("Введите месяц: "))
    for i in arrMonth:
        if month == i:
            flag = False
    if flag:
        print("Нет такого месяца.")

year = int(input("Введите год: "))


def date(d, m, y):
    if y % 4 == 0:
        arrMonth['февраль'] = 29
    else:
        arrMonth['февраль'] = 28
    if 0 < d <= arrMonth[m]:
        return True
    else:
        return False


print('Такой день: ' + str(date(day, month, year)))

'''Список [16, -17, 2, 78.7, False, False, {‘True’: True}, 555, 12, 23, 42, ‘DD’]
Функция, принимает на вход список -выбирает из него все int и float
-составить из него новый список, отсортированный от наименьшего значения большему'''

arrJob = [6, -17, 2, 78.7, False, False, {'True': True}, 555, 12, 23, 42, 'DD']


def funArrIntFloat(arr):
    arrTmp = []
    for i in arr:
        if type(i) == float or type(i) == int:
            arrTmp.append(i)
    arrTmp.sort()
    return arrTmp


print(funArrIntFloat(arrJob))
