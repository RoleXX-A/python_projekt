HELP = """
help - напечатать справку
add - добавить задачу в список(название задачи запрашиваем у пользователя)
show - напечатать все добавленные задачи
random - добавляем случайную задачу на сегодня
"""

random_task = "записаться на курс"
tasks = {}
run = True


def add_todo(date, task):
    if date in tasks:
        # дата есть в словаре, добавляем задачу к ключу date
        tasks[date].append(task)
    else:
        # даты нет в словаре, создаем запись с ключем date
        tasks[date] = []
        tasks[date] = [task]
    print("задача добавлена")

while run:
    command = input("Введите команду: ")

    if command == "help":
        print(HELP)
    elif command == "show":
        date = input("Введите дату для отображения списка ")
        if date in tasks:
            for task in tasks[date]:
                print('- ', task)
        else:
            print("Такой даты нет")
    elif command == "add":
        date = input("Введите дату задачи ")
        task = input("Введите название задачи ")
        add_todo(date, task)

    elif command == "random":
       add_todo("сегодня", random_task)
    else:
        print("неизвестная команда")
        break
print("Пока!")
