a = ' Hi'

f = open('data.txt', 'a')
f.write(a)
f.close()
f = open('data.txt')
text = f.read()
print(text)

