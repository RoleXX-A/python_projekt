from random import choice

print('Привет')
print('Я генерирую карту - ты угадываешь цвет масти')

card_number = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suit = ['Ч', 'Б', 'Т', 'П']  # ч,б - красные, т,п - черные

random_card_number = choice(card_number)
random_card_suit = choice(card_suit)

random_card = random_card_number + ' ' + random_card_suit
player_answer = input('Выберите вашу карту: ')

if player_answer == 'черный' and random_card_suit in ['Т', 'П']:
    print('Ответ верный! Выбранная карта ' + random_card)

elif player_answer == 'красный' and random_card_suit in ['Ч', 'Б']:
    print('Ответ верный! Ваша карта ' + random_card)

else:
    print('Ответ не верный! ' + random_card)
