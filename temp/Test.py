import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


def get_list_movies():
    soup = BeautifulSoup(requests.get('https://afisha.tut.by/film/').text, 'lxml')
    articles = soup.find_all('ul', {'class': ['b-lists list_afisha col-5']})
    return [art.find('a', {'class': ['name']}).find('span').get_text() for art in articles]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/movies1')
def movies():
    list_movies = get_list_movies()
    return render_template('movies.html', list_movies=list_movies)


def main():
    return 0


if __name__ == '__main__':
    app.run(debug=True)
