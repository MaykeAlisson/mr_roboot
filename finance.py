import requests


def get_price():
    res = requests.get('https://api.hgbrasil.com/finance?key=${env.keyHg}')
    if res.status_code == 200:
        modedas = res.json()['results']['currencies']
        dolar = modedas['USD']['buy']
        dolar_vari = modedas['USD']['variation']
        euro = modedas['EUR']['buy']
        euro_vari = modedas['EUR']['variation']
        bitcoin = modedas['BTC']['buy']
        bitcoin_vari = modedas['BTC']['variation']
        stocks = res.json()['results']['stocks']
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

    return 'Erro ao buscar informações!'
