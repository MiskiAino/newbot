import telebot
import random

from telebot.types import Message

TOKEN = '721378927:AAF3OX-i_oXfK0asbUJzDi5JhVVujShLomI'

bot = telebot.TeleBot(TOKEN)
USERS = set()


# удаление сообщение с ссылками
GROUP_ID = -256567579  # Ваш ID группы

@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == GROUP_ID)
def delete_links(message):
    for entity in message.entities:  # Пройдёмся по всем entities в поисках ссылок
        # url - обычная ссылка, text_link - ссылка, скрытая под текстом
        if entity.type in ["url","" "text_link"]:
            # Мы можем не проверять chat.id, он проверяется ещё в хэндлере
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return


# @bot.message_handler(commands=['start','help'])
# def command_handler(message: Message):
#     bot.reply_to(message, 'hello, im is helpless bot')
#
# @bot.message_handler(content_types=['text'])
# def echo_digits(message: Message):
#     reply = str(random.random())
#
#     if message.from_user.id in USERS:
#         reply = f"{message.from_user.username}, hello again"
#
#     bot.reply_to(message, reply)
#     USERS.add(message.from_user.id)
#
# @bot.message_handler(content_types=['sticker'])
# def sticker_handler(message: Message):
#     bot.reply_to(message, 'опять стикеры с оняме')



bot.polling(none_stop=True)
