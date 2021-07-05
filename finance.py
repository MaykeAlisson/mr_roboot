import requests
from datetime import date

from newsapi import NewsApiClient


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


def get_news(token):
    newsapi = NewsApiClient(api_key=token)

    top_headlines = newsapi.get_top_headlines(category='business',
                                              language='pt')

    status = top_headlines['status']

    def get_html(title, body):
        codigo_html = '''
        <html>
        <head>
        <title>News Finance</title>
        </head>
        <body>
        <center>
            <h1>{0}</h1>
            {1}       
        </center>
        </body>
        </html>
        '''.format(title, body)
        return codigo_html

    if status == 'ok':
        data_base = date.today().strftime("%m/%d/%y")
        noticias = top_headlines['articles']
        title = 'News Finance {}'.format(data_base)
        body = ''
        for noticia in noticias:
            ul = '''
            <ul>
            <p style="font-weight: bold; font-size: large; " ><span>{0}</span></p>
            <p style="font-weight: bold; margin: -10 !important;">
            <span>
            <a href="{1}"  style="text-decoration:none; color: #2E8B57;" >Saiba Mais</a>
            </span>
            </p>
            <p><span>Fonte: {2}</span></p>
            </ul>
            '''.format(noticia['title'], noticia['url'], noticia['source']['name'])
            body += str(ul)

        arq_html = open('finance.html', 'w')
        arq_html.write(get_html(title, body))
        arq_html.close()
