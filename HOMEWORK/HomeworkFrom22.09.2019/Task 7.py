"""Получить курс нескольких валют за текущую дату.
Сообщение в виде списка, вроде: «За 11.04.2019 курс 2.12 рублей за 1 Евро, 2.28… за 1 доллар».
http://www.nbrb.by/APIHelp/ExRates"""
import requests
import datetime


def get_money(cur_abbreviation):
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    rates = requests.get(url).json()
    for rate in rates:
        if rate['Cur_Abbreviation'] in (cur_abbreviation.upper()):
            return 'За {} курс {} рублей за {} {}'.format(datetime.datetime.now().date(), rate['Cur_OfficialRate'],
                                                          rate['Cur_Scale'], rate['Cur_Name'])
    return 'Нет такой валюты'


def main():
    print(get_money(input('Введите нужную валюту: ')))


if __name__ == '__main__':
    main()
