import telebot
import sqlite3
from tok import key

bot = telebot.TeleBot(key)
name = None
@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('test.db') # создание файла базы данных
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME varchar(50),
    pass varchar(50));
    ''')# создание информации в таблице(CREATE TABLE IF NOT EXISTS user - создание таблицы "user это имя таблицы
    # id, name, pass это колонки таблицы")

    conn.commit() #принятие изменений записанных в таблицу
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Привет, введите имя для регистрации')
    bot.register_next_step_handler(message, user_name) # переход на выполнение следующей функции

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Ведите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    data = (f'{name}', f'{password}')
    cur.execute(f'INSERT INTO user(name,pass) VALUES{data};')# записывает в таблицу введеные данные в соответствующие столбцы

    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей',callback_data = 'users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('test.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM user ORDER BY id DESC LIMIT 1') # выбирает из таблицы все столбцы
    users = cur.fetchall() # выводит все записи

    info = ''
    for el in users:
        info += f'Имя {el[1]} пароль {el[2]} \n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)



bot.polling(none_stop=True)