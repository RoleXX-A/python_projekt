Hellp = """Доступные команды:
help - вызов справки
add - добавить новую задачу
show - посмотреть список задач
exit - закрыть программу"""

tasks = []
run = True

while run:
    command = input('Введите команду: ')

    if command == 'help':
        print(Hellp)

    elif command == 'show':
        print(', '.join(tasks))

    elif command == 'add':
        task = input('Введите задачу ')
        tasks.append(task)
        print('Задача добавлена!')

    elif command == 'exit':
       run = False
print('Good Bye')