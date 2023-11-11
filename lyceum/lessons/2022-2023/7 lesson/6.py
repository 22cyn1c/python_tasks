a = input()
last_line = -1
d = 0
z = 0
while a != '':
    while a != 'Какой подарок?':
        if a == 'добрый':
            d += 1
            last_line = 1
        elif a == 'злой':
            z += 1
            last_line = 2
        a = input()
        if a == '':
            break
    if a == '':
        break
    if d > z and last_line == 1:
        print('серебряный шиллинг')
    elif z > d and last_line == 2:
        print('золотой')
    else:
        print('Ах, не знаю!')
        break
    a = input()
    d = 0
    z = 0