from bs4 import BeautifulSoup
import requests


def get_data_films():
    url = 'https://afisha.tut.by/film'
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    films = soup.find('div', class_='events-block js-cut_wrapper').find_all('li')
    data_films = list()

    for data in films:
        tmp = dict()
        tmp['name'] = data.find('img').get('alt')
        tmp['link'] = data.find('a').get('href')
        tmp['image'] = data.find('img').get('src')
        tmp['info'] = data.find('div').find('p').text
        data_films.append(tmp)
    return data_films
