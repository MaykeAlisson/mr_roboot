#!/usr/bin/env python3
import time
import telepot
from decouple import config
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

############################### ENV ############################################
TOKEN = config('TELEGRAN_TOKEN')
USER = config('TELEGRAN_USER')


############################### Bot ############################################

def handle(message):
    print(message)
    origin = message['chat']
    content_type, chat_type, chat_id = telepot.glance(message)
    if str(chat_id) != USER:
        bot.sendMessage(chat_id, 'Sinto muito {0}, mas eu só falo com meu mestre!'.format(origin['first_name']))
        return

    bot.sendMessage(chat_id, main_menu_message(), reply_markup=main_menu_keyboard())


def on_callback_query(message):
    query_id, from_id, query_data = telepot.glance(message, flavor='callback_query')

    def option(value):
        if value == 'fin':
            return bot.sendMessage(USER, first_menu_message(), reply_markup=first_menu_keyboard())
        elif value == 'dev':
            return bot.sendMessage(USER, second_menu_message(), reply_markup=second_menu_keyboard())
        elif value == 'out':
            return bot.sendMessage(USER, third_menu_message(), reply_markup=third_menu_keyboard())

    def optionsFinance(value):
        pass

    def optionsDevelop(value):
        pass

    def optionsOuthers(value):
        pass

    print('Callback Query:', query_id, from_id, query_data)

    option(query_data)
    optionsFinance(query_data)
    optionsDevelop(query_data)
    optionsOuthers(query_data)

    # bot.answerCallbackQuery(query_id, text='Got it')


############################ Keyboards #########################################


def main_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Finance', callback_data='fin')],
        [InlineKeyboardButton(text='Develop', callback_data='dev')],
        [InlineKeyboardButton(text='Others', callback_data='out')],
    ])
    return keyboard


def first_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Price', callback_data='fin_1')],
        [InlineKeyboardButton(text='Submenu 2-2', callback_data='fin_2')],
        [InlineKeyboardButton(text='Menu principal', callback_data='main')]
    ])
    return keyboard


def second_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Ip', callback_data='dev_1')],
        [InlineKeyboardButton(text='Storage', callback_data='dev_2')],
        [InlineKeyboardButton(text='Retornar menu', callback_data='main')]
    ])
    return keyboard


def third_menu_keyboard():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Submenu 3-1', callback_data='out_1')],
        [InlineKeyboardButton(text='Submenu 3-2', callback_data='out_2')],
        [InlineKeyboardButton(text='Menu principal', callback_data='main')]
    ])
    return keyboard


############################# Messages #########################################

def main_menu_message():
    return 'Select options :'


def first_menu_message():
    return 'Select options finance:'


def second_menu_message():
    return 'Select options develop:'


def third_menu_message():
    return 'Select options others:'


bot = telepot.Bot(TOKEN)

MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
