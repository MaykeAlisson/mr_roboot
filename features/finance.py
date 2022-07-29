import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_price(url):
    req_bored = requests.get(url)

    if req_bored.status_code != 200:
        return 'Requisição falhou, tente novamente!'

    modedas = req_bored.json()['results']['currencies']
    dolar = modedas['USD']['buy']
    dolar_vari = modedas['USD']['variation']
    euro = modedas['EUR']['buy']
    euro_vari = modedas['EUR']['variation']
    bitcoin = modedas['BTC']['buy']
    bitcoin_vari = modedas['BTC']['variation']
    stocks = req_bored.json()['results']['stocks']
    ibov = stocks['IBOVESPA']['points']
    ibov_vari = stocks['IBOVESPA']['variation']
    nasdaq = stocks['NASDAQ']['points']
    nasdaq_vari = stocks['NASDAQ']['variation']

    message = 'Dolar: {0} variação {1}\n' \
              'Euro: {2} variação {3}\n' \
              'Bitcoin: {4} variação {5}\n' \
              'Ibovespa: {6} variação {7}\n' \
              'Nasdaq: {8} variação {9}\n'.format(dolar, dolar_vari, euro, euro_vari, bitcoin, bitcoin_vari, ibov,
                                                  ibov_vari, nasdaq, nasdaq_vari)
    return message


def get_news():
    return 'Em breve!'


class Finance(object):

    def __init__(self):
        """[Resumo]
        Método construtor define valores globais.
        """
        self.url_base_hgb = 'https://api.hgbrasil.com/finance?key=${env.keyHg}'

        self.original_actions = ["price", "news"]

    def finance(self, update, context):
        """[Resumo]
        Função executada quando o comando '/finance' é utilizado no chat do telegram.
        """

        # Lista com as atividades para exibir nos botões
        actions = self.original_actions

        # Cria botões e define valor de callback para quando forem clicados
        keyboard = [[InlineKeyboardButton(actions[0], callback_data='0'),
                     InlineKeyboardButton(actions[1], callback_data='1')]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # Aciona botões com mensagem para escolher atividade
        update.message.reply_text('Por favor escolha um tipo de atividade:', reply_markup=reply_markup)

    def button(self, update, context):
        """[Resumo]
        Função acionada quando o botão é clicado.
        """
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        query.answer()

        def case_options(argument):
            switcher = {
                0: get_price(self.url_base_hgb),
                1: get_news()
            }
            return switcher.get(argument, "option not exist")

        result = case_options(int(query.data))

        query.edit_message_text(text=result)
