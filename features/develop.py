import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_ip():
    ip = os.popen("curl --max-time 60 --ipv4 icanhazip.com").read().strip()
    os.popen("curl http://freedns.afraid.org/dynamic/update.php?VmRDMHhhbTVlTWFvQ1p1UWpSOXU6MTgwNDk4NjA=")
    return ip


def get_storage():
    storage = os.popen('df -h').read().strip()
    return storage


class Develop(object):

    def __init__(self):
        """[Resumo]
        Método construtor define valores globais.
        """

        self.original_actions = ["ip", "storage"]

    def develop(self, update, context):
        """[Resumo]
        Função executada quando o comando '/develop' é utilizado no chat do telegram.
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
                0: get_ip(),
                1: get_storage()
            }
            return switcher.get(argument, "option not exist")

        result = case_options(int(query.data))

        query.edit_message_text(text=result)


