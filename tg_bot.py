import telebot
from tok import key
import webbrowser
from telebot import types

bot = telebot.TeleBot(key)

#bot.send_message(1013037331, 'Hi! I\'m a Bot!')

@bot.message_handler(commands=['start'])# Добавляение кнопок и приветсвия
def start(message):
    mark = types.ReplyKeyboardMarkup() # постоянные кнопки
    btn1 = types.KeyboardButton('Перейти на сайт школы')
    mark.row(btn1)
    btn2 = types.KeyboardButton('Удалить')
    btn3 = types.KeyboardButton('Получить файл')
    mark.row(btn2,btn3) # расположение кнопок



    #audio_file = open('./123.mp3','rb') # Отправка файла в ответ на команду
    #bot.send_audio(message.chat.id, audio_file, reply_markup=mark)






    bot.send_message(message.chat.id, 'Привет', reply_markup=mark)
    bot.register_next_step_handler(message, on_click) # выполнение функции после нажатия на кнопку "on_click - это выполняемая функция"


def on_click(message):
    if message.text == 'Перейти на сайт школы':
        bot.send_message(message.chat.id, 'open website')
        webbrowser.open('https://itmuose.by')

    elif message.text == 'Удалить':
        bot.send_message(message.chat.id, 'delete')
        bot.delete_message(message.chat.id, message.message_id - 3) #данная функция удаляет сообщение 3 от момента выолнения команды

    elif message.text == 'Получить файл': # отправка фото из интернета
        photo_file = ('https://img.freepik.com/free-photo/adorable-illustration-kittens-playing-forest-generative-ai_260559-483.jpg?t=st=1713446527~exp=1713450127~hmac=ed707ff772772900a755018f79a08e64d5da2c018b3262bbb6181bb02a702582&w=826')
        bot.send_photo(message.chat.id, photo_file)


@bot.message_handler(content_types=['photo']) #прием и ответ на фото в сообщении
def get_photo(message):
    mark = types.InlineKeyboardMarkup() # кнопки в тексте
    #mark.add(types.InlineKeyboardButton('Перейти на сайт школы', url='https://itmuose.by'))
    #mark.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    #mark.add(types.InlineKeyboardButton('Изменить', callback_data='edit'))

    mark.row(types.InlineKeyboardButton('Перейти на сайт школы', url='https://itmuose.by'))
    mark.row(types.InlineKeyboardButton('Удалить фото', callback_data='delete'),types.InlineKeyboardButton('Изменить', callback_data='edit'))
    bot.reply_to(message, 'Я получил фото', reply_markup=mark)

@bot.callback_query_handler(func = lambda callback:True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.id - 1)
    elif callback.data == 'edit':
        photo_file = open('C:/Users/User/YandexDisk/Загрузки/Акт.jpg', 'rb')
        bot.send_photo(callback.message.chat.id, photo_file)











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
