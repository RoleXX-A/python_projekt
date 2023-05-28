import random

points = [2, 3, 4, 6, 7, 8, 9, 10, 11]
player_one = []
player_two = []
name_first_player = input('Представьтес: ')
name_second_player = input('Представьтесь: ')
start_first = f'{name_first_player} возьми карту'
start_second = f'{name_second_player} возьми карту'

print(start_first)
player_one.append(random.choice(points))  # первая карта
print(f'вы набрали {sum(player_one)} очков')

while sum(player_one) <= 21:  # цикл первого игрока, пока не наберет 21 или не закончит брать карту
    print('продолжим играть? \n1: да \n2: нет')
    stage = int(input())
    if stage == 1:
        player_one.append(random.choice(points))
        print(sum(player_one))
    if stage == 2:
        print(f'вы набрали {sum(player_one)} очков \n')
        break
    elif sum(player_one) == 21:
        print('вы набрали 21 очко')
        break
    if sum(player_one) > 21:
        print(f'вы проиграли ')
        break

if sum(player_one) > 21:  # условие перехода к циклу второго игрока. Если выполнено, то второй игрок играет,
    # если нет то первый игрок проиграл
    print(f'выиграл {name_second_player}')
else:
    print(start_second)
    player_two.append(random.choice(points))  # второй игрок берет случайную карту
    print(f'вы набрали {sum(player_two)} очков')

    while sum(player_two) <= 21:  # цикл второго игрока
        print('продолжим играть? \n1: да \n2: нет')
        stage = int(input())
        if stage == 1:
            player_two.append(random.choice(points))
            print(sum(player_two))
        if stage == 2:
            print(f'вы набрали {sum(player_two)} очков')
            break
        elif sum(player_two) == 21:
            print('вы набрали 21 очко')
            break
        if sum(player_two) > 21:
            print(f'вы проиграли')
            break

    if sum(player_one) and sum(player_two) <= 21:  # условие выявляет победителя, на основании набранных очков
        if 21 == sum(player_one) or sum(player_one) > sum(player_two):
            print(f'выиграл {name_first_player}')
        elif sum(player_one) == sum(player_two):
            print('Ничья')
        else:
            print(f'выиграл {name_second_player}')
