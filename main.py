#!/usr/bin/env python3
from decouple import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from handler import listener, argument, unknown, finance_menu, develop_menu, others_menu, listener_finance, \
    listener_develop, listener_others

############################### ENV ############################################
TOKEN = config('TELEGRAN_TOKEN')

############################### Bot ############################################

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

# Escuta text menos oque e comand
listener_handler = MessageHandler(Filters.text & (~Filters.command), listener)
dispatcher.add_handler(listener_handler)
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
updater.dispatcher.add_handler(CallbackQueryHandler(listener_others, pattern='sub_out_*'))

updater.start_polling()

# run forever https://stackoverflow.com/questions/19571282/using-forever-js-with-python/19571283
