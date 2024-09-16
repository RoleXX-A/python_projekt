#7197734689:AAGSqJf_fPo-NA0aOePScjoVxoNHwWY3FsM
from openai import OpenAI
import telebot
from telebot import types
OPENAI_API_KEY = "sk-MMrfLGaE1bjKSpdZzo8u6tu7P5s1gOB2"
TELEGRAM_BOT_TOKEN = "7197734689:AAGSqJf_fPo-NA0aOePScjoVxoNHwWY3FsM"
# Инициализация клиента API OpenAI с вашим API ключом
client = OpenAI(
    api_key= OPENAI_API_KEY,
    base_url="https://api.proxyapi.ru/openai/v1",
)

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start','help'])

def send_welcome(message):
    photo_file = ('https://img.freepik.com/free-photo/adorable-illustration-kittens-playing-forest-generative-ai_260559-483.jpg?t=st=1713446527~exp=1713450127~hmac=ed707ff772772900a755018f79a08e64d5da2c018b3262bbb6181bb02a702582&w=826')
    bot.send_photo(message.chat.id, photo_file)
    bot.send_message(message.chat.id,"Привет Я бот, который использует нейросеть ChatGPT для ответов. Можешь задать любой вопрос.")

# Список для хранения истории разговора
def chat_with_ai(message_text):
    messages = [{"role": "user", "content": message_text}]
        # Запрос ввода пользователя
    chat_completion = client.chat.completions.create(
        model='gpt-3.5-turbo-1106',
        messages=messages
    )
        #Ответ от AI
    response_message = chat_completion.choices[0].message.content
    return response_message

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    response = chat_with_ai(message.text)
    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)
