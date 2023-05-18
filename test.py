import random


points = [2, 3, 4, 6, 7, 8, 9, 10, 11]
player_one = []
player_two = []

print('игрок 1 возьмите карту')

player_one.append(random.choice(points))
print(f'вы набрали {sum(player_one)} очков')

while sum(player_one) <= 21:
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
        print(f'вы проиграли {sum(player_one)}')
        break

print('игрок 2 возьмите карту')
player_two.append(random.choice(points))
print(f'вы набрали {sum(player_two)} очков')

while sum(player_two) <= 21:
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
        print(f'вы проиграли {sum(player_two)}')
        break

if sum(player_one) and sum(player_two) <= 21:
    if 21 == sum(player_one) > sum(player_two):
        print('выиграл игрок 1')
    else:
        print('выиграл игрок 2')
