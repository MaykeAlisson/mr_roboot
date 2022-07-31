import os
import requests


def get_ip():
    ip = os.popen("curl --max-time 60 --ipv4 icanhazip.com").read().strip()
    os.popen("curl http://freedns.afraid.org/dynamic/update.php?VmRDMHhhbTVlTWFvQ1p1UWpSOXU6MTgwNDk4NjA=")
    return ip


def get_storage():
    storage = os.popen('df -h').read().strip()
    return storage


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


class Callback(object):

    def __init__(self):
        """[Resumo]
        Método construtor define valores globais.
        """

        self.url_base_hgb = 'https://api.hgbrasil.com/finance?key=${env.keyHg}'

    def button(self, update, context):
        """[Resumo]
        Função acionada quando o botão é clicado.
        """
        query = update.callback_query

        # CallbackQueries need to be answered, even if no notification to the user is needed
        query.answer()

        def case_options(argument):
            if argument == 'ip':
                return get_ip()

            if argument == 'storage':
                return get_storage()

            if argument == 'price':
                return get_price(self.url_base_hgb)

            if argument == 'news':
                return get_news()

            return "option not exist"

        result = case_options(query.data)

        query.edit_message_text(text=result)
