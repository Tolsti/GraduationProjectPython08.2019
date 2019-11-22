from bs4 import BeautifulSoup
from flask import Flask, url_for, render_template
import requests
from get_films import data_films

app = Flask(__name__)

soup = BeautifulSoup(requests.get('https://afisha.tut.by/film/').text, 'lxml')


# data_films = list()
# films = soup.find('div', class_='events-block js-cut_wrapper').find_all('a', class_='media')
# for data in films:
#     tmp = dict()
#     tmp['name'] = data.find('img').get('alt')
#     tmp['link'] = data.get('href')
#     tmp['image'] = data.find('img').get('src')
#     data_films.append(tmp)


# @app.route('/')
# def hello():
#     return 'Hello World'

@app.route('/')
def index():
    return 'Hello'


@app.route('/movies')
def movies():
    movies_list = data_films
    return render_template('movies.html', data_films=data_films)


@app.route('/login')
def login():
    pass


@app.route('/user/<username>')
def profile(username):
    pass


# @app.route('login', method=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         do_the_login()
#     else:
#         show_the_login_from()


# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='John Snow'))


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     return 'Post %d' % post_id


# @app.route('/hell')
# def hell():
#     return 'BOOO!!!'


# @app.route('/movies')
# def movies():
#     return "soup.find('div', class_='events-block js-cut_wrapper').find_all('a', class_='media')[0].get('herf')"


# def main():
#     return 0


if __name__ == '__main__':
    app.run(debug=True)
