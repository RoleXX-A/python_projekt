import telebot
from PycharmProjects.python_projekt.tg import bot


def start_button(message, keyboard=None):
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
    # red_button = telebot.types.KeyboardButton('🟥')  # создаем кнопку для красной карты
    # black_button = telebot.types.KeyboardButton('⬛️')  # создаем кнопку для черной карты

    # Добавляем кнопки клавиатуры
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row(six_buttonR, six_buttonB)
    keyboard.row(seven_buttonR, seven_buttonB)
    keyboard.row(eight_buttonR, eight_buttonB)
    keyboard.row(nine_buttonR, nine_buttonB)
    keyboard.row(ten_buttonR, ten_buttonB)
    keyboard.row(jack_buttonR, jack_buttonB)
    keyboard.row(quin_buttonR, quin_buttonB)
    keyboard.row(king_buttonR, king_buttonB)
    keyboard.row(ace_buttonR, ace_buttonB)
    # reply_markup = keyboard передает клавиатуру в сообщение пользователю
    bot.send_message(message.chat.id,reply_markup=keyboard)
    bot.register_next_step_handler(message)