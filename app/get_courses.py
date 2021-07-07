import requests, flask_wtf, wtforms, wtforms.validators
import datetime
import jinja2

#хардкод УРЛ-ов, в остальном - чисто, красиво
def get_currency_rates_data(date=str(datetime.datetime.now().date())):
    try:
        url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0&onDate=' + date
    except TypeError:
        url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    except jinja2.exceptions.UndefinedError:
        return 'Нет такой даты'
    return requests.get(url).json()


class CoursesForm(flask_wtf.FlaskForm):
    date = wtforms.StringField('Дата', validators=[wtforms.validators.DataRequired()])
    button = wtforms.SubmitField('Найти')
