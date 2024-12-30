import telebot

from random import choice

secret_key = '6652756332:AAFuzhaFCwTis93M6uaOtZsfj6Q1kh369_k'

bot = telebot.TeleBot(secret_key)


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()  # создаем клавиатуру
    six_button = telebot.types.KeyboardButton('6')
    seven_button = telebot.types.KeyboardButton('7')
    eight_button = telebot.types.KeyboardButton('8')
    nine_button = telebot.types.KeyboardButton('9')
    ten_button = telebot.types.KeyboardButton('10')
    jack_button = telebot.types.KeyboardButton('В')
    quin_button = telebot.types.KeyboardButton('Д')
    king_button = telebot.types.KeyboardButton('К')
    ace_button = telebot.types.KeyboardButton('Т')
    red_button = telebot.types.KeyboardButton('🟥')  # создаем кнопку для красной карты
    black_button = telebot.types.KeyboardButton('⬛️')  # создаем кнопку для черной карты

    # Добавляем кнопки клавиатуры
    keyboard.row(six_button)
    keyboard.row(seven_button)
    keyboard.row(eight_button)
    keyboard.row(nine_button)
    keyboard.row(ten_button)
    keyboard.row(jack_button)
    keyboard.row(quin_button)
    keyboard.row(king_button)
    keyboard.row(ace_button)
    keyboard.row(red_button)
    keyboard.row(black_button)
    # reply_markup=keyboard - передает клавиатуру в сообщение пользователю
    bot.send_message(message.chat.id, 'Угадай цвет масти карты: 🟥 или ⬛️',
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, answer_card)


# функция обработки ответа игрока
def answer_card(message):
    suit, number = genarate_random_card()
    random_card = number + '' + suit
    # проверка ответа игрока
    if message.text == '🟥' and suit in ('Ч', 'Б'):
        bot.send_message(message.chat.id, 'Ответ верный! Выбранная карта ' + random_card)
    elif message.text == '⬛️' and suit in ('Т', 'П'):
        bot.send_message(message.chat.id, 'Ответ верный! Выбранная карта ' + random_card)
    else:
        bot.send_message(message.chat.id, 'Ответ не верный! ' + random_card)

    start(message)  # зацикливание процесса игры


# функция добавляет и выбирает карты из колоды карт ( ч,б - красные, т,п - черные)
def genarate_random_card():
    card_number = ['6', '7', '8', '9', '10', 'В', 'Д', 'K', 'Т']
    card_suit = ['Ч', 'Б', 'Т', 'П']

    random_card_suit = choice(card_suit)
    random_card_number = choice(card_number)

    return random_card_suit, random_card_number


# бесконечный запуск бота
bot.infinity_polling()
