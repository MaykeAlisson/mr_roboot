from decouple import config

############################### ENV ############################################
USER = config('TELEGRAN_USER')


############################### HANDLERS ########################################
def listener(update, context):
    origin = update['message']['chat']
    if str(update.effective_chat.id) != USER:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Sinto muito {0}, mas eu só falo com meu mestre!'.format(origin['first_name']))
        return


def start(update, context):
    context.bot.send_message(chat_id=USER, text='ola mundo /start')


def argument(update, context):
    arg = context.args
    context.bot.send_message(chat_id=USER, text=arg)


def unknown(update, context):
    context.bot.send_message(chat_id=USER, text='Desculpe comando não reconhecido!')
