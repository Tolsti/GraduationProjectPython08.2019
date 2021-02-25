import requests

from bot_config import time


class TelegramBot:

    def __init__(self, token):
        self.token = token
        self.url = f'https://api.telegram.org/bot{self.token}/'

    def get_updates(self):
        method = 'getUpdates'
        req = requests.get(self.url + method)
        return req.json()

    def get_message(self):
        data = self.get_updates()
        last_message = data['result'][-1]['message']
        chat_id = last_message['chat']['id']
        text = last_message['text']
        message = {'chat_id': chat_id, 'text': text}
        return message

    def send_message(self, chat_id, text):
        method = 'sendMessage'
        params = {'chat_id': chat_id, 'text': text}
        response = requests.post(self.url + method, params)
        return response


class MoneyBot(TelegramBot):

    def __init__(self, token):
        super().__init__(token)
        self.money_url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'

    def get_money(self):
        response = requests.get(self.money_url).json()
        usd_price = eur_price = pln_price = 'NOT_FOUND'
        for p in list(response):
            if p['Cur_Abbreviation'] == 'USD':
                usd_price = p['Cur_OfficialRate']
            if p['Cur_Abbreviation'] == 'EUR':
                eur_price = p['Cur_OfficialRate']
            if p['Cur_Abbreviation'] == 'PLN':
                pln_price = p['Cur_OfficialRate']
        return f'Cost of one BYN today - {usd_price} USD, {eur_price} EUR, {pln_price} PLN'
        # rates = requests.get(self.money_url).json()
        # for rate in rates:
        #     if rate['Cur_Abbreviation'] in (cur_abbreviation.upper()):
        #         return '{} За {} {} {} бел. рублей'.format(datetime.datetime.now().date(), rate['Cur_Scale'],
        #                                                    rate['Cur_Name'], rate['Cur_OfficialRate'])
        # return 'Нет такой валюты'

    def record_message_to_file(self):
        with open('messages/message' + ''.join(str(time).split(':')) + '.txt', 'w') as message_file:
            last_user_message = self.get_updates()['result'][-2]['message']['text']
            message_file.write(last_user_message + '\n')


