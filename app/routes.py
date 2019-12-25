import datetime, requests
from flask import render_template, url_for, flash, redirect
from app import app, get_data_films, get_data_courses, CoursesForm, get_data_weather_city, CityForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/courses', methods=['GET', 'POST'])
def courses():
    form = CoursesForm(csrf_enabled=False)
    return render_template('courses.html', rates=get_data_courses(form.date.data), form=form)


@app.route('/movies')
def movies():
    return render_template('movies.html', data_now=datetime.datetime.now().date(), data_films=get_data_films())


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    form = CityForm(csrf_enabled=False)
    return render_template('weather.html', data_now=datetime.datetime.now().date(),
                           data_weather=get_data_weather_city(form.city.data), form=form)
if __name__ == '__main__':
    app.run('127.0.0.1')#(debug=True)