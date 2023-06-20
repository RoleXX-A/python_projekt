kirilica = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z',
            'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r',
            's', 't', 'u', 'f', 'h', 'c', 'ch', 'sh', 'shch',
            '', 'y', '', 'e', 'yu', 'ya'

]
start_index = ord('а')

title = 'Python - лучший язык программирования'
slug = ''

for s in title.lower():
    if 'а'<= s <= 'я':
        slug += kirilica[ord(s) - start_index]
    elif s == 'ё':
        slug = 'yo'
    elif s in ' ,.:;!?':
        slug += '-'
    else:
        slug += s

while slug.count('--'):
    slug = slug.replace('--', '-')

print(slug)