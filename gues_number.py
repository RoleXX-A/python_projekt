from random import randint

print('Я загадываю число, а ты отгадываешь за три попытки. Играем до 3 побед!')
random_number = randint(0, 10)
win_python = 0
win_player = 0


def guess_number(win_player, win_python):
    player_number = int(input('Предложи свое число: '))
    if player_number < random_number:
        print('Твое число меньше моего, попробуй еще')
    elif player_number > random_number:
        print('Твое число больше моего, попробуй еще')
    else:
        print('Ты угадал')
        win_player += 1
    if player_number != random_number:
        print('Ты не угадал')
        win_python += 1


