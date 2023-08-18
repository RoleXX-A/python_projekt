number = input()
number_1 = ['+', '7', '(', 'x', 'x', 'x', ')', 'x', 'x', 'x', '-', 'x', 'x', '-', 'x', 'x']
lstn = []
lstn1 = []
if len(number) == len(number_1):
    if number[0] == '+' and number[1] == '7':
        if number[2] == '(' and number[6] == ')' and number[10] == '-' and number[13] == '-':
            for i, j in enumerate(number):
                if number[i].isdigit():
                    lstn.append(i)
            del lstn[0]

for k, l in enumerate(number_1):
    if number_1[k].isalpha():
        if number_1[1] == '7':
            lstn1.append(k)

print(lstn)
print(lstn1)
if lstn == lstn1:
    print('ДА')
else:
    print('НЕТ')
