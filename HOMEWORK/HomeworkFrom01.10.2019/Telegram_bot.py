import requests
import re
import time
import datetime
from itertools import permutations

token = '810680445:AAFfn2x6gfxylbH3pA75fk4DXvNiAoRWPIg'

URL = 'https://api.telegram.org/bot' + token + '/'

global last_upd
last_upd = 0


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_message():
    data = get_updates()

    last_obj = data['result'][-1]
    curr_update_id = last_obj['update_id']

    update_id = last_obj['update_id']
    global last_upd
    if last_upd != curr_update_id:
        last_upd = curr_update_id
        chat_id = last_obj['message']['chat']['id']
        message_text = last_obj['message']['text']
        message = {'chat_id': chat_id, 'text': message_text}
        return message
    # chat_id = data['result'][-1]['message']['chat']['id']
    # message_text = data['result'][-1]['message']['text']

    # chat_id = last_obj['message']['chat']['id']
    # message_text = last_obj['message']['text']
    #
    # message = {'chat_id': chat_id, 'text': message_text}
    # return message
    return None


def send_message(chat_id, text):
    url = URL + 'sendmessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)


def main():
    while True:
        answer = get_message()
        if answer is not None:
            chat_id = answer['chat_id']
            text = answer['text']
            print(text)
            if '//' in re.findall('\S\S', text):
                # if len(time) < 8:
                send_message(chat_id, search_wow(''.join(re.findall(r'\w+', text))))
            elif '/' in re.findall('\S', text):
                send_message(chat_id, get_money(''.join(re.findall(r'\w+', text)).upper()))
            # if '/usd' == text:
            #     send_message(chat_id, get_money('/usd'))
            # if '/eur' == text:
            #     send_message(chat_id, get_money('/eur'))
            # if '/rub' == text:
            #     send_message(chat_id, get_money('/rub'))
        else:
            continue
            time.sleep(3)


def get_money(cur_abbreviation):
    url = 'http://www.nbrb.by/API/ExRates/Rates?Periodicity=0'
    rates = requests.get(url).json()
    for rate in rates:
        if rate['Cur_Abbreviation'] in (cur_abbreviation.upper()):
            return '{} За {} {} {} бел. рублей'.format(datetime.datetime.now().date(), rate['Cur_Scale'],
                                                       rate['Cur_Name'], rate['Cur_OfficialRate'])
    return 'Нет такой валюты'


def search_wow(set_word):
    print(len(set_word))
    if len(set_word) >= 8:
        return 'Слишком длинное слово'
    set_word.lower()
    all_combinations = list()
    found_words = list()
    count = len(set_word)
    while count >= 3:
        for i in permutations(set_word, count):
            all_combinations.append(''.join(i))
        count -= 1
    print(len(all_combinations), all_combinations)
    file = open('TMP.txt').read().splitlines()
    for i in file:
        if i in all_combinations:
            found_words.append(i)
    found_words.sort()
    count = len(set_word)
    tmp_list = list()
    while count >= 3:
        for i in found_words:
            if len(i) == count:
                tmp_list.append(i)
        count -= 1
    found_words = tmp_list[::-1]
    return found_words


if __name__ == '__main__':
    main()
