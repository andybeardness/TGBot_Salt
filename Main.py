import telebot
import Salt
from Secrets import Secret

# активация бота в телеграм и прокси
SECRETS = Secret.Scrt()

TOKEN = SECRETS.get_token()
telebot.apihelper.proxy = SECRETS.get_proxy()

bot = telebot.TeleBot(TOKEN)

# инициализация модуля для изменения текста
VS = Salt.Vowels_S()

# реакция бота на любые текстовые сообщения
@bot.message_handler(content_types=['text'])
def change_msg(message):

    # присвоение переменной уже измененного текста
    posolen_private = VS.salt(message.text)

    # текстовое сообщение было отправлено в чате или суперчате
    if message.chat.type in ('supergroup', 'group'):

        # сообщение отправил сам пользователь
        if message.forward_from is None:
            posolen_group = f'@{message.from_user.username} :\n{posolen_private}'
            bot.send_message(message.chat.id, posolen_group)
            bot.delete_message(message.chat.id, message.message_id)

        # сообщение переслано пользователем
        else:
            posolen_forwared = f'@{message.from_user.username} :\n>> Переслано от @{message.forward_from.username} :\n{posolen_private}'
            bot.send_message(message.chat.id, posolen_forwared)
            bot.delete_message(message.chat.id, message.message_id)

    # текстовое сообщение отправлено непосредственно боту
    elif message.chat.type == 'private':
        bot.reply_to(message, posolen_private)

bot.polling(none_stop=True)