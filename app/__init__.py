from flask import Flask
from .get_films import get_films_data
from .get_courses import get_currency_rates_data, CoursesForm
from .get_weather import get_city_weather_data, CityForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

from app import routes
