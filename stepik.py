city = list(map(str, input().lower().split()))
end_city = ['ь', 'ъ', 'ы']
out = 'ДА'

for i in range(len(city)-1):
    if city[i][-1] in end_city:
        if city[i+1][0] != city[i][-2]:
            out = 'НЕТ'
            break
    else:
        if city[i+1][0] != city[i][-1]:
            out = 'НЕТ'
print(out)

