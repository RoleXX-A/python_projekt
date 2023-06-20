# str_1 = input()

# if not 'ра' in str_1:
# print(-1)
# else:
# for i in range(0, len(str_1)):
#   if str_1[i] == 'р' and str_1[i+1] == 'а':
#      print(i, end=' ')


number = input()
number_1 = ['+', 7, '(', 'x', 'x', 'x', ')', 'x', 'x', 'x', '-', 'x', 'x', '-', 'x', 'x']

if len(number) == len(number_1):
    if number[0] == '+' and number_1[1] == 7:
        print(number)

