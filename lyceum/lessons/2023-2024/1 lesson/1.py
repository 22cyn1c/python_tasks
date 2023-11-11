a = input()
b = input()
if a == 'камень' and b == 'ножницы' or a == 'ножницы' and b == 'бумага' or\
        a == 'бумага' and b == 'камень':
    print('первый')
elif b == 'камень' and a == 'ножницы' or b == 'ножницы' and a == 'бумага' or\
        b == 'бумага' and a == 'камень':
    print('второй')
elif a == b:
    print('ничья')