import datetime
from flask import render_template, url_for
from app import app
from app.get_films import data_films
from app.get_courses import rates
from app.get_weather import get_weather_city



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/courses')
def courses():
    return render_template('courses.html', data_now = datetime.datetime.now().date(), rates = rates)


@app.route('/movies')
def movies():
    return render_template('movies.html', data_now = datetime.datetime.now().date(), data_films = data_films)


@app.route('/weather')
def weather():
    return render_template('weather.html', data_now = datetime.datetime.now().date(), data_weather = get_weather_city())
print(get_weather_city())