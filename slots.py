import random


def spin_row():
    symbols = ['🍒','🍉','🍋','🔔','⭐']

    return [random.choice(symbols) for _ in range(3)]
def print_row(row):
    print('*************')
    print(' | '.join(row))
    print('*************')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return  bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 100


    print('*****************************\n '
          'Добро пожаловать в игру SLOTS\n '
          'Symbols: 🍒 🍉 🍋 🔔 ⭐\n'
          '*****************************')

    while balance > 0:
        print(f'Ваш баланс составляет: {balance}')

        bet = input('Сделайте вашу ставку:')

        if not bet.isdigit():
            print('Пожалуйста введите число!')
            continue

        bet = int(bet)

        if bet > balance:
            print('Недостаточно средств')
            continue

        if bet <= 0:
            print('Ставка должна быть больше 0')
            continue

        balance -= bet

        row = spin_row()
        print('Spinning...\n')
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f'Ты выиграл: {payout}')
        else:
            print('Ты проиграл в этом раунде')

        balance += payout

        play_again = input('Хочешь сыграть еще? (Y/N) ').upper()

        if play_again != 'Y':
            break

    print(f'Игра окончена. Твой выигрыш составил: {balance} ')

if __name__ == '__main__':
    main()