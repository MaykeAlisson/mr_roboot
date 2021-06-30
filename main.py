#!/usr/bin/env python3
from decouple import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

# from handler import listener, start, argument, unknown

############################### ENV ############################################
TOKEN = config('TELEGRAN_TOKEN')

USER = config('TELEGRAN_USER')

############################### Bot ############################################

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher


def listener(update, context):
    origin = update['message']['chat']
    if str(update.effective_chat.id) != USER:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Sinto muito {0}, mas eu só falo com meu mestre!'.format(origin['first_name']))
        return

    context.bot.send_message(chat_id=USER, text=menu_title(), reply_markup=main_menu_keyboard())


def start(update, context):
    context.bot.send_message(chat_id=USER, text='ola mundo /start')


def argument(update, context):
    arg = context.args
    context.bot.send_message(chat_id=USER, text=arg)


def unknown(update, context):
    context.bot.send_message(chat_id=USER, text='Desculpe comando não reconhecido!')


############################ Keyboards #########################################

def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Finance', callback_data='fin')],
                [InlineKeyboardButton('Develop', callback_data='dev')],
                [InlineKeyboardButton('Others', callback_data='out')]]
    return InlineKeyboardMarkup(keyboard)


def finance_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Price', callback_data='sub_fin_1')],
                [InlineKeyboardButton('News', callback_data='sub_fin_2')]]
    return InlineKeyboardMarkup(keyboard)


def develop_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Ip', callback_data='sub_dev_1')],
                [InlineKeyboardButton('Storage', callback_data='sub_dev_2')]]
    return InlineKeyboardMarkup(keyboard)


def finance_menu(update, context):
    context.bot.send_message(chat_id=USER, text=menu_title(), reply_markup=finance_menu_keyboard())


def develop_menu(update, context):
    context.bot.send_message(chat_id=USER, text=menu_title(), reply_markup=develop_menu_keyboard())


def others_menu(update, context):
    return context.bot.send_message(chat_id=USER, text='Em Breve!')


def menu_title():
    return 'Menu :'


def listener_finance(update, context):
    query = update.callback_query.data
    print(query)


def listener_develop(update, context):
    query = update.callback_query.data
    print(query)


# Escuta text menos oque e comand
listener_handler = MessageHandler(Filters.text & (~Filters.command), listener)
dispatcher.add_handler(listener_handler)
# Escuta o comando start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
# Escuta o comando argument e recebe argumento
argument_handler = CommandHandler('argument', argument)
dispatcher.add_handler(argument_handler)
# se não encontrar comando correspondente
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(finance_menu, pattern='fin'))
updater.dispatcher.add_handler(CallbackQueryHandler(develop_menu, pattern='dev'))
updater.dispatcher.add_handler(CallbackQueryHandler(others_menu, pattern='out'))
updater.dispatcher.add_handler(CallbackQueryHandler(listener_finance, pattern='sub_fin_*'))
updater.dispatcher.add_handler(CallbackQueryHandler(listener_develop, pattern='sub_dev_*'))

updater.start_polling()

# run forever https://stackoverflow.com/questions/19571282/using-forever-js-with-python/19571283
