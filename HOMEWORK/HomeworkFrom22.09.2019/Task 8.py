"""Получить список статей хабра за месяц. https://habr.com/top/monthly/"""

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # list_of_articles = soup.find_all('a','post__title_link')
    list_of_articles = [section.string for section in soup.find_all('a', 'post__title_link')]
    return list_of_articles


def main():
    url = 'https://habr.com/top/monthly/'
    for i in get_data(get_html(url)):
        print(i)


if __name__ == '__main__':
    main()
