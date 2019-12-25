import telebot, re
from app import get_films_data, get_currency_rates_data, get_city_weather_data

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
                            #запихнуть столько логики в одну функцию - неудачная идея
                            #если следовать ООП - нужно делить на классы
                            #если следовать ФП - делить на функции, причем основная логика должна быть чистой
                            #(без сайд-эффектов) 
def get_text_messages(message):
    #обрати внимание на часто используемый код
    #например re.findall(<ЧТО-ТО>, message.text)
    #answer(что-то>)
    #читабельности и простоты это не добавляет, поэтому желательно сделать фунции для таких шаблонных действий
    def pattern_search(pattern): return re.findall(pattern, message.text)
    def answer(answer_text): return answer(answer_text)

    if message.text == '/help':
        answer(
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
    #films
    elif message.text == '/films':
        films = ''
        for film in get_films_data():
            films += film['name'] + '\n'
        answer(films)
    #weather forecast
    elif '/weather' in pattern_search(r'\S{8}'):
        try:
            city = pattern_search(r'\w+')[1]
        except IndexError:
            city = 'Minsk'
        try:
            weather_data = get_city_weather_data(city)
            weather = 'Город: '         + str(weather_data['city']) + \
                      '\nТемпература: ' + str(weather_data['temp']) + \
                      '\nВлажность: '   + str(weather_data['humidity']) + \
                      '\nДавление: '    + str(weather_data['pressure'])
        except KeyError:
            weather = 'Нет такого города'
        answer(weather)

    #Currency_rates
    elif '/' in pattern_search(r'\S'):
        try:
            courses_date = '{}-{}-{}'.format(
                           pattern_search((r'\w+')[1],
                           pattern_search(r'\w+')[2],
                           pattern_search(r'\w+')[3])
        except IndexError:
            courses_date = get_currency_rates_data()[0]['Date'][0:-9]
        courses = 'Курс валюты на ' + courses_date
        # multiple currencies rates
        if '/courses' in pattern_search(r'\S{8}'):
            for rate in get_currency_rates_data(courses_date):
                courses += '\nЗа {scale} {of_currency} {rate_to_BYN} бел. рублей'.format(
                                scale       =rate['Cur_Scale'],
                                of_currency =rate['Cur_Name'],
                                rate_to_BYN =rate['Cur_OfficialRate'])
            answer(courses)
        # single currency rate
        elif '/' in pattern_search(r'\S'):
            for rate in get_currency_rates_data(courses_date):
                if pattern_search(r'\w+')[0].upper() == rate['Cur_Abbreviation']:
                    answer(courses + '\nЗа {scale} {of_currency} {rate_to_BYN} бел. рублей'.format(
                                scale       =rate['Cur_Scale'],
                                of_currency =rate['Cur_Name'],
                                rate_to_BYN =rate['Cur_OfficialRate']))
                    break
            else:
                answer('Я тебя не понимаю. Напиши /help.')
    else:
        answer('Я тебя не понимаю. Напиши /help.')


bot.polling(none_stop=True, interval=0)
