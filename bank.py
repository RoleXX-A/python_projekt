def show_balance(balance):
    print('**********************************')
    print(f'Баланс вашего счета:{balance:.2f}')
    print('**********************************')

def deposit():
    print('**********************************')
    amount = float(input('Введи сумму пополнения: '))
    print('**********************************')

    if amount < 0:
        print('Некоректная сумма')
        return 0
    else:
        return amount

def withdraw(balance):
    print('**********************************')
    amount = float(input('Введи сумму перевода: '))
    print('**********************************')

    if amount > balance:
        print('**********************************')
        print('Недостаточно средст для перевода.')
        print('**********************************')
        return 0
    elif amount < 0:
        print('**********************************')
        print('Невозможно перевести отрицательную сумму.')
        print('**********************************')
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print('**********************************')
        print(f"Программа поплонения счета.\n1. Баланс \n2. Пополнение счета \n3. Перевод средств \n4. Выход")
        print('**********************************')
        choice = input("Выберите необходимую операцию: ")
        print('**********************************')
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print('**********************************')
            print('Введите корректную команду!')
            print('**********************************')

    print('**********************************')
    print("Спасибо! Ждем вас снова!")
    print('**********************************')

if __name__ == '__main__':
    main()