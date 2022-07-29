class Unknow(object):

    def __init__(self):
        """[Resumo]
        Método construtor define valores globais.
        """

    def unknow(self, update, context):
        return context.bot.send_message(chat_id=update.effective_chat.id, text='Desculpe comando não reconhecido!')
