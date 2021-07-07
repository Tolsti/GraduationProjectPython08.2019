from bs4 import BeautifulSoup
import requests

#лаконично, красиво, читаемо. Только пара нюансов о хардкоде и временных переменных
def get_films_data():
    url = 'https://afisha.tut.by/film' #хардкод URL-ов и прочегое - не есть хорошо. И по PEP8 константы именуются капсом
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    films = soup.find('div', class_='events-block js-cut_wrapper').find_all('li')
    films_data = [] #квадратик читабельнее

    for data in films:
        film = {        #вместо временной переменной лушче переменная, отражающая логику действий
        'name' : data.find('img').get('alt'),
        'link' : data.find('a').get('href'),
        'image': data.find('img').get('src'),
        'info' : data.find('div').find('p').text
               }
        films_data.append(film) #добавление film в data_films выглядит осмысленнее, чем добавление tmp туда же
    return films_data
