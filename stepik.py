def vowels_in_string(str):
    lst = ['e', 'o', 'u', 'i', 'a','y','q', 'E','Y','U','I','O','A','Q']
    lst1 = []
    for i in str:
        if i in lst:
            lst1.append(i)
    print(len(lst1))


vowels_in_string('foncms')
