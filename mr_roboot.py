from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from decouple import config
from features.finance import Finance
from features.unknow import Unknow
from features.develop import Develop
from features.others import Others
import logging

# Importa variavel de ambiente token
TOKEN = config('TELEGRAN_TOKEN')
# Importa variavel de ambiente id do usuario
USER = config('TELEGRAN_USER')

# Define padrão de log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=comands)


class Bot(object):
    """[Resumo]
    A classe bot possui a estrutura necessária para utilizar os métodos
    das classes das funcionalidades e configurar os comandos que serão
    exibidos no bot.
    """

    global comands
    comands = 'Bem vindo!\nEstes são os comandos disponiveis:\n/develop funções dev\n' \
              '/finance funções financeira\n' \
              '/news funções noticias\n' \
              '/others funções utilitarias'

    def __init__(self):
        """[Resumo]
        O método construtor define o token do bot, cria um Updater com o token, inicializa
        o dispatcher, que é o responsável por gerenciar todos os comandos e ações, e enfim,
        também cria os objetos de classe das funcionalidades.
        """
        bot_token = TOKEN

        self.updater = Updater(token=bot_token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        self.finance = Finance()
        self.develop = Develop()
        self.others = Others()
        self.unknown = Unknow()

    def run(self):
        """[Resumo]
        Função cria todos os comandos do bot, são jogados no dispatcher e depois inicializado.
        """

        # Escuta texto que não seja comando
        listener_handler = MessageHandler(Filters.text & (~Filters.command), start)

        # Comando finance
        finance_handler = CommandHandler('finance', self.finance.finance)
        finance_callback = CallbackQueryHandler(self.finance.button)

        # Comando develop
        develop_handler = CommandHandler('develop', self.develop.develop)
        develop_callback = CallbackQueryHandler(self.develop.button)

        # Comandos do others
        others_handler = CommandHandler('others', self.others.others)
        url_handler = CommandHandler('url', self.others.url)

        # Comandos unknown
        unknown_handler = MessageHandler(Filters.command, self.unknown.unknow)

        # Dispatchers do bot
        self.dispatcher.add_handler(listener_handler)

        # Dispatchers da finances
        self.dispatcher.add_handler(finance_handler)
        self.dispatcher.add_handler(finance_callback)

        # Dispatchers da develop
        self.dispatcher.add_handler(develop_handler)
        self.dispatcher.add_handler(develop_callback)

        # Dispatchers da others
        self.dispatcher.add_handler(others_handler)
        self.dispatcher.add_handler(url_handler)

        # Dispatchers do unknown
        self.dispatcher.add_handler(unknown_handler)

        # Inicia a execução do bot
        self.updater.start_polling()

        # Roda o bot até apertar CTRL + C ou receber um SIGNAL
        self.updater.idle()

    '''
        IMPLEMENTAÇÃO DOS COMANDOS BÁSICOS DO BOT
    '''
