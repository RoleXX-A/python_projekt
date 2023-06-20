str_1 = input()

if not 'ра' in str_1:
    print(-1)
else:
    for i in range(0, len(str_1)):
        if str_1[i] == 'р' and str_1[i+1] == 'а':
            print(i, end=' ')




