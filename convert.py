import telebot
from tok import key
from telebot import types
import requests


cash = 0
bot = telebot.TeleBot(key)

@bot.message_handler(commands=['start'])
def func(message):
    bot.send_message(message.chat.id, 'Привет, введите сумму')
    bot.register_next_step_handler(message,func2)

def func2(message):
    global cash

    try:
        cash = float(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат')
        return
    if cash > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('RUB/USD', callback_data='rub/usd')
        btn2 = types.InlineKeyboardButton('RUB/EUR', callback_data='rub/eur')
        btn3 = types.InlineKeyboardButton('Другое', callback_data='else')
        markup.add(btn1,btn2,btn3)
        bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, 'Введите число больше нуля')
        bot.register_next_step_handler(message,func2)



@bot.callback_query_handler(func = lambda call:True)
def callback_message(call):
    if call.data != 'else':
        val = call.data.upper().split('/')
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url) #запрос курса валют
        data = response.json()
        rate = data['Valute']['USD']['Value']
        res = cash * rate
        bot.send_message(call.message.chat.id, f'Итог {round(res,2)} курс перевода {rate} ')
        bot.register_next_step_handler(call.message,func2)
    else:
        bot.send_message(call.message.chat.id, f'Введите пару значений через /')
        bot.register_next_step_handler(call.message, my_cur)

def my_cur(message):
    val = message.text.upper().split('/')
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url)
    data = response.json()
    rate = data['Valute']['USD']['Value']
    res = cash * rate
    bot.send_message(message.chat.id, f'Итог {round(res,2)} курс перевода {rate} ')
    bot.register_next_step_handler(message, func2)

bot.polling()