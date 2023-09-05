# защита от дурака
# Уагадать масть
# Угадать карту
# Выбрать сложность
# Количество раундов

if __name__ == "__main__":
    from random import choice

    print('Привет! Давай сыграем в игру.\nЯ загадываю карту, а ты должен ее угадать.'
          '\nЕсть три режима сложности')
    level_one = 'цвет карты'
    level_two = 'значение и цвет'
    level_three = 'значение и масть'
    level = int(input('Выбери уровень: '))
    rounds = 0
    card_number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    card_suit = ['Ч', 'Б', 'Т', 'П']  # ч,б - красные, т,п - черные
# мешаем карты
    random_card_number = choice(card_number)
    random_card_suit = choice(card_suit)
    random_card = random_card_number + ' ' + random_card_suit

    if level == 1:
        print('Это легкий уровень, достаточно угадать только цвет')
        while rounds < 5:
            rounds += 1
            player_answer = input('Выбери  карту: ')
            if player_answer == 'черный' and random_card in ['Т', 'П']:
                print('Ответ верный! Выбранная карта ' + random_card)

            elif player_answer == 'красный' and random_card in ['Ч', 'Б']:
                print('Ответ верный! Ваша карта ' + random_card)

            else:
                print('Ответ не верный! ' + random_card)
    elif level == 2:
        print('Это немного сложнее, угадай цвет и значение карты')
    elif level == 3:
        print('Это самый сложный уровень, угадай масть карты и ее значение')
    else:
        print('на таком уровне даже я не смогу угадать, выбери полегче.')



    print('игра окончена')
