from telegram import InlineKeyboardButton, InlineKeyboardMarkup


class Finance(object):

    def __init__(self):
        """[Resumo]
        Método construtor define valores globais.
        """

        self.original_actions = ["price", "news"]

    def finance(self, update, context):
        """[Resumo]
        Função executada quando o comando '/finance' é utilizado no chat do telegram.
        """

        # Lista com as atividades para exibir nos botões
        actions = self.original_actions

        # Cria botões e define valor de callback para quando forem clicados
        keyboard = [[InlineKeyboardButton(actions[0], callback_data=actions[0]),
                     InlineKeyboardButton(actions[1], callback_data=actions[1])]]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # Aciona botões com mensagem para escolher atividade
        update.message.reply_text('Por favor escolha um tipo de atividade:', reply_markup=reply_markup)

