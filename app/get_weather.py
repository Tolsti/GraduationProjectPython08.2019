import requests, flask_wtf, wtforms, wtforms.validators


# appid = '94d8b74c4d0c302754e1af1f42419289'
# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}


def get_data_weather_city(city):
    if city is None or city == '':
        city = 'Minsk'
    url = 'http://api.openweathermap.org/data/2.5/weather?appid='
    app_id = "94d8b74c4d0c302754e1af1f42419289"
    data = dict()
    weather_city = requests.get(url + '{}&q={}&units=metric'.format(app_id, city)).json()
    try:
        data['city'] = weather_city['name']
        data['temp'] = weather_city['main']['temp']
        data['temp_max'] = weather_city['main']['temp_max']
        data['temp_min'] = weather_city['main']['temp_min']
        data['humidity'] = weather_city['main']['humidity']
        data['pressure'] = weather_city['main']['pressure']
    except KeyError:
        data['city'] = 'Нет такого города'
    return data


class CityForm(flask_wtf.FlaskForm):
    city = wtforms.StringField('Название города', validators=[wtforms.validators.DataRequired()])
    button = wtforms.SubmitField('Найти')
