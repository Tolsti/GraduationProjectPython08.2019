import datetime, requests
from flask import render_template, url_for, flash, redirect
from app import app, get_films_data, get_currency_rates_data, CoursesForm, get_city_weather_data, CityForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/courses', methods=['GET', 'POST']) #курс валют - currency rate. Стоит уделять внимание бизнес-терминологии
def courses():
    form = CoursesForm(csrf_enabled=False)
    return render_template('courses.html', rates=get_currency_rates_data(form.date.data), form=form)


@app.route('/movies')
def movies():
    return render_template('movies.html', data_now=datetime.datetime.now().date(), data_films=get_films_data())


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    form = CityForm(csrf_enabled=False)
    return render_template('weather.html', data_now=datetime.datetime.now().date(),
                           data_weather=get_city_weather_data(form.city.data), form=form)
#if __name__ == '__main__':
    #app.run('127.0.0.1')#(debug=True)