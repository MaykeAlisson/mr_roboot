from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from decouple import config
import logging

# Importa variavel de ambiente token
TOKEN = config('TELEGRAN_TOKEN')
# Importa variavel de ambiente id do usuario
USER = config('TELEGRAN_USER')

# Define padrão de log
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

class Bot(object):
    """[Resumo]
    A classe bot possui a estrutura necessária para utilizar os métodos
    das classes das funcionalidades e configurar os comandos que serão
    exibidos no bot.
    """

    global comands
    comands = 'Bem vindo!\nEstes são os comandos disponiveis:\n/develop funções dev\n'\
              '/finance funções financeira\n'\
              '/news funções noticias\n'\
              '/outher funções utilitarias'

    def __init__(self):
        """[Resumo]
        O método construtor define o token do bot, cria um Updater com o token, inicializa
        o dispatcher, que é o responsável por gerenciar todos os comandos e ações, e enfim,
        também cria os objetos de classe das funcionalidades.
        """
        bot_token = TOKEN

        self.updater = Updater(token=bot_token, use_context=True)
        self.dispatcher = self.updater.dispatcher

        # self.pokedex = Pokedex()
        # self.url_short = Urlshort()
        # self.bored = Bored()

    def run(self):
        """[Resumo]
        Função cria todos os comandos do bot, são jogados no dispatcher e depois inicializado.
        """
        # Comandos básicos do bot
        # start_handler = CommandHandler('start', self.start)

        # Escuta texto que não seja comando
        listener_handler = MessageHandler(Filters.text & (~Filters.command), self.start)


        # Comandos da pokédex
        # pokedex_handler = CommandHandler('pokedex', self.pokedex.pokedex)
        # habilidades_handler = CommandHandler('habilidades', self.pokedex.habilidades)
        # moves_handler = CommandHandler('moves', self.pokedex.moves)

        # Comandos do encurtador de URL
        # url_handler = CommandHandler('url', self.url_short.url)

        # Comandos do desentediador
        # bored_handler = CommandHandler('bored', self.bored.bored)
        # button_callback = CallbackQueryHandler(self.bored.button)
        # participantes_handler = CommandHandler('participantes', self.bored.participantes)

        # Dispatchers do bot
        self.dispatcher.add_handler(listener_handler)

        # Dispatchers da pokédex
        # self.dispatcher.add_handler(pokedex_handler)
        # self.dispatcher.add_handler(habilidades_handler)
        # self.dispatcher.add_handler(moves_handler)

        # Dispatchers do encurtador de URL
        # self.dispatcher.add_handler(url_handler)

        # Dispatchers do desentediador
        # self.dispatcher.add_handler(bored_handler)
        # self.dispatcher.add_handler(button_callback)
        # self.dispatcher.add_handler(participantes_handler)

        # Inicia a execução do bot
        self.updater.start_polling()

        # Roda o bot até apertar CTRL + C ou receber um SIGNAL
        self.updater.idle()

    '''
        IMPLEMENTAÇÃO DOS COMANDOS BÁSICOS DO BOT
    '''

    def start(self, update, context):
        origin = update['message']['chat']
        if str(update.effective_chat.id) != USER:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Sinto muito {0}\nmas eu só falo com meu mestre!'.format(origin['first_name']))
            return

        context.bot.send_message(chat_id=USER,
                                 text=comands)