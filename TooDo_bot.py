import telebot

token =""

bot = telebot.TeleBot(token)

HELP = """
/help - напечатать справку
/add - добавить задачу в список(название задачи запрашиваем у пользователя)
/show - напечатать все добавленные задачи
/random - добавляем случайную задачу на сегодня
"""
tasks = {}

def add_todo(date, task):
    if date in tasks:
        #дата есть в словаре
        #добавляем задачу
        tasks[date].append(task)
    else:
        #даты нет в словаре
        #создаем запись с ключем date
        tasks[date] = []
        tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

