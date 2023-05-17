import random

points = [2, 3, 4, 6, 7, 8, 9, 10, 11]
player_one = []
player_two = []

print('игрок 1 возбмите карту')
game_over = 'много вы проиграли'


player_one.append(random.choice(points))
print(f'вы набрали {sum(player_one)} очков')
while sum(player_one) != 21:
    print('продолжим играть?')
    stage = input()
    if stage == 'да':
        player_one.append(random.choice(points))
        print(sum(player_one))
    if stage == 'себе':
        print(f'вы набрали {sum(player_one)} очков')
        break
    elif sum(player_one) == 21:
        print('вы набрали 21 очко')
    if sum(player_one) > 21:
        print(game_over)
        break