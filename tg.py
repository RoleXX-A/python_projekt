import telebot

from random import choice


secret_key = '6652756332:AAFuzhaFCwTis93M6uaOtZsfj6Q1kh369_k'

bot = telebot.TeleBot(secret_key)


@bot.message_handler(commands=['start'])
def start(message, keyboard=None):
    six_buttonR = telebot.types.KeyboardButton('6🟥')
    six_buttonB = telebot.types.KeyboardButton('6⬛️')
    seven_buttonR = telebot.types.KeyboardButton('7🟥')
    seven_buttonB = telebot.types.KeyboardButton('7⬛️')
    eight_buttonR = telebot.types.KeyboardButton('8🟥')
    eight_buttonB = telebot.types.KeyboardButton('8⬛️')
    nine_buttonR = telebot.types.KeyboardButton('9🟥')
    nine_buttonB = telebot.types.KeyboardButton('9⬛️')
    ten_buttonR = telebot.types.KeyboardButton('10🟥')
    ten_buttonB = telebot.types.KeyboardButton('10⬛️')
    jack_buttonR = telebot.types.KeyboardButton('В🟥')
    jack_buttonB = telebot.types.KeyboardButton('В⬛️')
    quin_buttonR = telebot.types.KeyboardButton('Д🟥')
    quin_buttonB = telebot.types.KeyboardButton('Д⬛️')
    king_buttonR = telebot.types.KeyboardButton('К🟥')
    king_buttonB = telebot.types.KeyboardButton('К⬛️')
    ace_buttonR = telebot.types.KeyboardButton('Т🟥')
    ace_buttonB = telebot.types.KeyboardButton('Т⬛️')
    #red_button = telebot.types.KeyboardButton('🟥')  # создаем кнопку для красной карты
    #black_button = telebot.types.KeyboardButton('⬛️')  # создаем кнопку для черной карты

    # Добавляем кнопки клавиатуры
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row(six_buttonR, six_buttonB)
    keyboard.row(seven_buttonR, seven_buttonB)
    keyboard.row(eight_buttonR, eight_buttonB)
    keyboard.row(nine_buttonR, nine_buttonB)
    keyboard.row(ten_buttonR, ten_buttonB)
    keyboard.row(jack_buttonR, jack_buttonB)
    keyboard.row(quin_buttonR, quin_buttonB)
    keyboard.row(king_buttonR,king_buttonB)
    keyboard.row(ace_buttonR, ace_buttonB)
    #reply_markup = keyboard передает клавиатуру в сообщение пользователю
    bot.send_message(message.chat.id,'Угадай цвет масти карты: 🟥 или ⬛️',
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, answer_card)


# функция обработки ответа игрока
def answer_card(message):
    suit, number = genarate_random_card()
    random_card = number + '' + suit
    # проверка ответа игрока
    if message.text == '6🟥' and message.text == random_card:
        bot.send_message(message.chat.id, 'Ответ верный! Выбранная карта ' + random_card)
    elif message.text == '⬛️' and suit in ('Т', 'П'):
        bot.send_message(message.chat.id, 'Ответ верный! Выбранная карта ' + random_card)
    else:
        bot.send_message(message.chat.id, 'Ответ не верный! ' + random_card)

    start(message) # зацикливание процесса игры


# функция добавляет и выбирает карты из колоды карт ( ч,б - красные, т,п - черные)
def genarate_random_card():
    card_number = ['6', '7', '8', '9', '10', 'В', 'Д', 'K', 'Т']
    card_suit = ['🟥', 'Б', 'Т', 'П']

    random_card_suit = choice(card_suit)
    random_card_number = choice(card_number)

    return random_card_suit, random_card_number

# бесконечный запуск бота
bot.infinity_polling()
