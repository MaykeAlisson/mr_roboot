#!/usr/bin/env python3
import time
from decouple import config
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

############################### ENV ############################################
TOKEN = config('TELEGRAN_TOKEN')
USER = config('TELEGRAN_USER')

############################### Const ##########################################

MENU = 'Menu'


############################### Bot ############################################

def handle(message):
    print(message)
    origin = message['chat']
    content_type, chat_type, chat_id = telepot.glance(message)
    if str(chat_id) != USER:
        bot.sendMessage(chat_id, 'Sinto muito {0}, mas eu só falo com meu mestre!'.format(origin['first_name']))
        return

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Finanças', callback_data='fin')],
        [InlineKeyboardButton(text='Develop', callback_data='dev')],
        [InlineKeyboardButton(text='Outros', callback_data='out')],
    ])

    bot.sendMessage(chat_id, main_menu_message(), reply_markup=keyboard)


def on_callback_query(message):
    query_id, from_id, query_data = telepot.glance(message, flavor='callback_query')

    def option(query_data):
        return {
            'fin': print("fin"),
            'dev': print('dev'),
            'out': print('out'),
        }[query_data]

    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')


def main_menu_message():
    return '{0} :'.format(MENU)


bot = telepot.Bot(TOKEN)

MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
