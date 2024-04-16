import telebot
from tok import key
import webbrowser

bot = telebot.TeleBot(key)

#bot.send_message(1013037331, 'Hi! I\'m a Bot!')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello')


@bot.message_handler(commands=['full_info'])
def full_info(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler(commands=['hello'])
def user_hello(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')


@bot.message_handler(commands=['site'])
def site(message):
    webbrowser.open('https://itmuose.by')


@bot.message_handler()
def chat_check(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Приветствую')


    elif message.text.lower() in ['ид', 'id']:
        bot.reply_to(message, f'ID чата - {message.from_user.id}')


bot.polling()
