import requests
from pprint import pprint


# appid = '94d8b74c4d0c302754e1af1f42419289'
# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}

def get_weather_city(city='Minsk'):
    app_id = "94d8b74c4d0c302754e1af1f42419289"
    return requests.get(
        'http://api.openweathermap.org/data/2.5/weather?appid={}&q={}&units=metric'.format(app_id, city)).json()

print(get_weather_city()['main']['temp'])

