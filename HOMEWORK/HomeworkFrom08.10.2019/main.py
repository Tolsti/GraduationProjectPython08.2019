from bot import MoneyBot
from bot_config import token
from utils import logg_this


def main():
    test_bot = MoneyBot(token)
    money = test_bot.get_money()
    answer = test_bot.get_message()
    logg_this(answer)
    chat_id = answer['chat_id']
    text = answer['text']

    if text == '/course':
        test_bot.send_message(chat_id, money)

    if text == '/write':
        test_bot.record_message_to_file(answer)
        test_bot.send_message(chat_id, 'done')

    else:
        test_bot.send_message(chat_id, 'Echo' + text)


test_for_bot = MoneyBot(token)
test_money = test_for_bot.get_money()
test_answer = test_for_bot.get_message()
test_recorder = test_for_bot.record_message_to_file()

if __name__ == '__main__':
    main()
