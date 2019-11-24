import requests
from pprint import pprint


# appid = '94d8b74c4d0c302754e1af1f42419289'
# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
# pro.openweathermap.org/data/2.5/forecast/hourly?id=524901

def get_weather_city(city = 'Minsk'):
    app_id = "94d8b74c4d0c302754e1af1f42419289"
    data = dict()
    weather_city = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}&units=metric'.format(app_id, city)).json()
    data['city'] = weather_city['name']
    data['temp'] = weather_city['main']['temp']
    data['temp_max'] = weather_city['main']['temp_max']
    data['temp_min'] = weather_city['main']['temp_min']
    data['humidity'] = weather_city['main']['humidity']
    data['pressure'] = weather_city['main']['pressure']
    return data


def get_weather_hours(city = 'Minsk'):
    app_id = "94d8b74c4d0c302754e1af1f42419289"
    weather_city = requests.get(
        'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}&units=metric'.format(app_id, city)).json()
    return weather_city
