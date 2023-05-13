month_day31 = [1, 3, 5, 7, 8, 10, 12]
month_day30 = [4, 6, 9, 11]
month_day28 = [2]

month, day = map(int, input().split())

if month in month_day31 and month != 3:
    if day > 1:
        if day < 31:
            print(f'{month:02}.{day - 1:02} {month:02}.{day + 1:02}')
    if day == 1:
        if month == 8:
            print(f'{month - 1:02}.{31} {month:02}.{day + 1:02}')
        else:
            print(f'{month - 1:02}.{30} {month:02}.{day + 1:02}')
    elif day == 31:
        print(f'{month:02}.{day - 1:02} {month + 1:02}.{1:02}')

if month == 3:
    if day > 1:
        if day < 31:
            print(f'{month:02}.{day - 1:02} {month:02}.{day + 1:02}')
    if day == 1:
        print(f'{month - 1:02}.{28} {month:02}.{day + 1:02}')
    elif day == 31:
        print(f'{month:02}.{day - 1:02} {month + 1:02}.{1:02}')

if month in month_day30:
    if day > 1:
        if day < 30:
            print(f'{month:02}.{day - 1:02} {month:02}.{day + 1:02}')
    if day == 1:
        print(f'{month - 1:03}.{31} {month:02}.{day + 1:02}')
    if day == 30:
        print(f'{month:02}.{day - 1:02} {month + 1:02}.{1:02}')
if month in month_day28:
    if day > 1:
        if day < 28:
            print(f'{month:02}.{day - 1:02} {month:02}.{day + 1:02}')
    if day == 1:
        print(f'{month - 1:03}.{31} {month:02}.{day + 1:02}')
    if day == 28:
        print(f'{month:02}.{day - 1:02} {month + 1:02}.{1:02}')
