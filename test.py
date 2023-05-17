import random

points = [2, 3, 4, 6, 7, 8, 9, 10, 11]
player_one = []
player_two = []

print('игрок 1 возбмите карту')
pause = 'продолжим играть? выберите "еще" или "хватит"'
game_over = 'много вы проиграли'

player_one.append(random.choice(points))
print(*player_one)
while sum(player_one) <= 21:
    print(pause)
    stage = input()
    if stage == 'еще':
        player_one.append(random.choice(points))
        print(sum(player_one))
    if stage == 'хватит':
        print(f'вы набрали {sum(player_one)} очков')
        break
    elif sum(player_one) == 21:
        print('вы набрали 21 очко')
    print(game_over)