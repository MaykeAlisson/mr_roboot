from decouple import config
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from develop import get_ip, get_storage
from finance import get_price

############################### ENV ############################################
USER = config('TELEGRAN_USER')


############################### VAR ############################################
menu = ''


############################### HANDLERS ########################################
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


def others_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Dowloand YouTube', callback_data='sub_out_1')]]
    return InlineKeyboardMarkup(keyboard)


############################ MENU #########################################

def finance_menu(update, context):
    global menu
    menu = 'Finance'
    context.bot.send_message(chat_id=USER, text=menu_title(), reply_markup=finance_menu_keyboard())


def develop_menu(update, context):
    global menu
    menu = 'Develop'
    context.bot.send_message(chat_id=USER, text=menu_title(), reply_markup=develop_menu_keyboard())


def others_menu(update, context):
    global menu
    menu = 'Others'
    context.bot.send_message(chat_id=USER, text=menu_title(), reply_markup=others_menu_keyboard())
    # return context.bot.send_message(chat_id=USER, text='Em Breve!')


def menu_title():
    return 'Menu {0}:'.format(menu)


############################ SUB MENU #########################################

def listener_finance(update, context):
    query = update.callback_query.data
    print(query)


def listener_develop(update, context):
    query = update.callback_query.data
    print(query)
    if str(query) == 'sub_dev_1':
        print('seu ip: ', get_ip())
        return
    if str(query) == 'sub_dev_2':
        print('seu storage: ', get_storage())
        return


def listener_others(update, context):
    query = update.callback_query.data
    print(query)
