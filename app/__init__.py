from flask import Flask
from .get_films import get_data_films
from .get_courses import get_data_courses, CoursesForm
from .get_weather import get_data_weather_city, CityForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes
