from openai import OpenAI
import telebot
import datetime
from telebot import types
from tok import *


# Создаем словарь для хранения дат, когда пользователь задавал вопрос
question_dates = {}

question_counter = 0
max_questions = 10  # Максимальное количество вопросов, которые пользователь может задать

# Инициализация клиента API OpenAI с вашим API ключом
client = OpenAI(
    api_key=open_ai_key,
    base_url="https://api.proxyapi.ru/openai/v1",
)
bot = telebot.TeleBot(key)

def can_ask_question(user_id):
    # Проверяем, задавал ли пользователь вопрос сегодня максимльно возможно количество раз
    if user_id in question_dates and question_counter == max_questions:
        today = datetime.date.today()
        last_question_date = question_dates[user_id]
        if last_question_date == today:
            return False  # Пользователь уже израсходовал лимит сообщений на сагодня
    return True  # Пользователь может задать вопрос

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    mark = types.InlineKeyboardMarkup()
    mark.add(types.InlineKeyboardButton('Начать общение 💬', callback_data='bot'))
    mark.add(types.InlineKeyboardButton('Курс валют 💷 💴 💶', callback_data='exchange_rate'),types.InlineKeyboardButton('Конвертация💷=>💶', callback_data='convert_value'))
    photo_file = (
        'https://media.wired.com/photos/66425c483aeee12d6ca99835/master/w_1920,c_limit/New-ChatGPT-Tier-Gear-GettyImages-2151457871.jpg')
    bot.send_photo(message.chat.id, photo_file)
    bot.send_message(message.chat.id,
                     "Привет👋  Я бот 🤖, который использует нейросеть ChatGPT для ответов. Можешь задать любой вопрос или о чем-то поговорить!"
                     "\n\nТеперь у меня есть новый навык, я могу подсказать курс валют 💷 💴 💶 , а так же сделать их конвертацию."
                     , reply_markup=mark)
@bot.callback_query_handler(func=lambda callback: callback.data == 'bot')
def new_answer(callback):
        bot.send_message(callback.message.chat.id, 'Чем могу тебе помочь❓')


def chat_with_ai(message_text):# функция запроса информации от пользователя
    messages = [{"role": "user", "content": message_text}]
    # Запрос ввода пользователя
    chat_completion = client.chat.completions.create(
        model='gpt-3.5-turbo-1106',
        messages=messages
    )
    # Ответ от AI
    response_message = chat_completion.choices[0].message.content
    return response_message

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    global question_counter  # Добавляем переменную question_counter как глобальную для изменения значения в функции
    user_id = message.from_user.id
    if question_counter < max_questions and can_ask_question(user_id):  # Проверяем, не задан ли пользователем максимальное количество вопросов в день
        response = chat_with_ai(message.text)
        bot.send_message(message.chat.id, response)
        question_counter += 1  # Увеличиваем счетчик заданных вопросов на 1
        # Обновляем дату последнего вопроса для пользователя
        question_dates[user_id] = datetime.date.today()
    else:
        bot.send_message(message.chat.id, "Очень жаль 😔, но на сегодня вы израсходовали лимит запросов."
                                          " Возвращайтесь завтра 👋")

@bot.callback_query_handler(func=lambda callback: callback.data == 'exchange_rate')#вызов функции курса валют
def exchange_rate(callback):
        bot.send_message(callback.message.chat.id, "Очень жаль 😔, но на сегодня вы израсходовали лимит запросов."
                                          " Возвращайтесь завтра 👋")


bot.polling(none_stop=True)
