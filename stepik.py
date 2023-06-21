# str_1 = input()

# if not 'ра' in str_1:
# print(-1)
# else:
# for i in range(0, len(str_1)):
#   if str_1[i] == 'р' and str_1[i+1] == 'а':
#      print(i, end=' ')


number = input()
number_1 = ['+', '7', '(', 'x', 'x', 'x', ')', 'x', 'x', 'x', '-', 'x', 'x', '-', 'x', 'x']
lstn = []
lstn1 = []
if len(number) == len(number_1):  # проверям на равность длины строки
    if number[0] == '+' and number[1] == '7':
        if number[2] == '(' and number[6] == ')' and number[10] == '-' and number[13] == '-':  # проверки на символы в маске номера
            for i, j in enumerate(number):
                if number[i].isdigit():  # выбираем числа и добавляем их в список
                    lstn.append(i)
            del lstn[0]  # удаляем первый элемент(не разобрался как его не считать) он нам не нужен

for k, l in enumerate(number_1):
    if number_1[k].isalpha():
        if number_1[1] == '7':
            lstn1.append(k)  # выбираем все символы с буквами и 7 и добавляем в другой список

if lstn == lstn1:  # сравнили списки
    print('ДА')
else:
    print('НЕТ')
