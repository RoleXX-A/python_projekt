def vowels_in_string(str):
    lst = ['e', 'o']
    lst1 = []
    for i in str:
        if i in lst:
            lst1.append(i)
    print(len(lst1))

vowels_in_string('foncms')