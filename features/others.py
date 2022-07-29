import requests


class Others(object):
    """[Resumo]
       A classe Others possui todos os comandos utilitarios.
       """

    global comands
    comands = 'Estes são os comandos disponiveis:\n' \
              '/url encurtador de url'

    def __init__(self):
        """[Resumo]
        Método construtor define valores globais.
        """
        self.url_base_short = 'https://cleanuri.com//api/v1/shorten'

    def others(self, update, context):
        """[Resumo]
        Função executada quando o comando '/others' é utilizado no chat do telegram.
        """

        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=comands)

    def url(self, update, context):
        """[Resumo]
        Função executada quando o comando '/url link_url' é utilizado no chat do telegram.
        """

        # Se quem acionou não colocar nenhum argumento no comando
        if not context.args:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Coloque a URL depois do comando!')
            return

        # Constrói body com a url para enviar à API
        url = context.args[0]
        data = {
            "url": url
        }

        req_url = requests.post(self.url_base_short, data=data)

        # Se a requisição deu errado, retorna mensagem de erro
        if req_url.status_code != 200:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='URL inválida! (Experimente com https:// ou http:// antes)')
            return

        # Se a requisição deu certo, coleta 'hashid' do encurtador e retorna URL pronta
        else:
            url_curta = req_url.json()['result_url']

            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Sua url encurtada: ' + url_curta)
            print(req_url.json())
