import requests, flask_wtf, wtforms, wtforms.validators


# appid = '94d8b74c4d0c302754e1af1f42419289'
# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}


def get_city_weather_data(city='Minsk'): #get_city_weather_data - информация о погоде в городе. data weather city - город погодной информации.
    if not city: # 0, None, False, '' - в логических выражениях эквивалентны False. (x == None) то же, что и (not x)
        city = 'Minsk'         # Пустая строка существует в python в единственном экзепляре, поэтому сравнивать с пустой строкой так же можно через is
    url = 'http://api.openweathermap.org/data/2.5/weather?appid=' #хардкод. Подобные константы следует выносить в отдельный файл
    app_id = "94d8b74c4d0c302754e1af1f42419289"

    city_weather = requests.get(url + '{}&q={}&units=metric'.format(app_id, city)).json()

    city_weather_data = {} #идентификатор должен быть говорящим, кроме редких исключений. Не бойся сделать его чуть длиннее
    try:
        city_weather_data = {
            'city': city_weather['name'],
            'temp': city_weather['main']['temp'],
        'temp_max': city_weather['main']['temp_max'],
        'temp_min': city_weather['main']['temp_min'],
        'humidity': city_weather['main']['humidity'],
        'pressure': city_weather['main']['pressure']
                 }
    except KeyError:
        city_weather_data['city'] = 'Нет такого города'
    return city_weather_data


class CityForm(flask_wtf.FlaskForm):
    city = wtforms.StringField('Название города', validators=[wtforms.validators.DataRequired()])
    button = wtforms.SubmitField('Найти')
