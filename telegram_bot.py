import telebot, re
from app import get_data_films, get_data_courses, get_data_weather_city

token = '810680445:AAFfn2x6gfxylbH3pA75fk4DXvNiAoRWPIg'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, чем я могу тебе помочь?\n'
                                      'Могу показать:\n'
                                      '-Курс валют на сегодня или конкретную дату.\n'
                                      '-Погода на сегодня в Минске или другом городе.\n'
                                      '-Что показывают сегодня в кинотеатрах.\n'
                                      '/help')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id,
                         '-Курс валют на сегодня:\n'
                         '/courses,\n'
                         '/usd, /eur, /rub и другие.\n'
                         'Курс валют по дате:\n'
                         '/courses 2015-11-22\n'
                         '/usd 2015-11-22\n'
                         '-Погода на сегодня в Минске:\n'
                         '/weather\n'
                         'Погода в другом городе\n'
                         '/weather Moscow\n'
                         '-В кинотеатрах сегодня:\n'
                         '/films')
    elif message.text == '/films':
        films = ''
        for film in get_data_films():
            films += film['name'] + '\n'
        bot.send_message(message.from_user.id, films)
    elif '/weather' in re.findall(r'\S{8}', message.text):
        try:
            city = re.findall(r'\w+', message.text)[1]
        except IndexError:
            city = 'Minsk'
        try:
            weather = 'Город: ' + str(get_data_weather_city(city)['city']) + \
                      '\nТемпература: ' + str(get_data_weather_city(city)['temp']) + \
                      '\nВлажность: ' + str(get_data_weather_city(city)['humidity']) + \
                      '\nДавление: ' + str(get_data_weather_city(city)['pressure'])
        except KeyError:
            weather = 'Нет такого города'
        bot.send_message(message.from_user.id, weather)
    elif '/' in re.findall(r'\S', message.text):
        try:
            courses_date = re.findall(r'\w+', message.text)[1] + '-' + \
                           re.findall(r'\w+', message.text)[2] + '-' + \
                           re.findall(r'\w+', message.text)[3]
        except IndexError:
            courses_date = get_data_courses()[0]['Date'][0:-9]
        courses = 'Курс валюты на ' + courses_date
        if '/courses' in re.findall(r'\S{8}', message.text):
            for rate in get_data_courses(courses_date):
                courses += '\nЗа ' + str(rate['Cur_Scale']) + ' ' + str(rate['Cur_Name']) + \
                           ' ' + str(rate['Cur_OfficialRate']) + ' бел. рублей'
            bot.send_message(message.from_user.id, courses)
        elif '/' in re.findall(r'\S', message.text):
            for rate in get_data_courses(courses_date):
                if re.findall(r'\w+', message.text)[0].upper() == rate['Cur_Abbreviation']:
                    bot.send_message(message.from_user.id, courses + '\n' +
                                     'За ' + str(rate['Cur_Scale']) + ' ' + str(rate['Cur_Name']) +
                                     ' ' + str(rate['Cur_OfficialRate']) + ' бел. рублей')
                    break
            else:
                bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')
    else:
        bot.send_message(message.from_user.id, 'Я тебя не понимаю. Напиши /help.')


bot.polling(none_stop=True, interval=0)
