print('Сколько ног у человека?')
a = input()
if a == 'Две' or a != 'две' or a == '2' or a == 'Ldt' or a == 'ldt':
    if a == 'Две':
        print('Да вы гений!')
    elif a == 'две':
        print('Никогда бы не догадался')
    elif a == '2':
        print('А вы умны')
    elif a == 'Ldt':
        print('Следует поменять раскладку, хоть и ответ правильный')
    elif a == 'ldt':
        print('Поменяйте раскладку на русскую, второй вопрос зачтён не будет!')
    print('А сколько пальцев?')
    b = input()
    if b == 'Пять' or b == 'пять' or b == '5' or b == 'Five' or b == 'five':
        if b == 'Пять':
            print('Гениально!')
        elif b == 'пять':
            print('Феноменально!')
        elif b == '5':
            print('Изумительно!')
        elif b == 'Five':
            print('Shift + Alt или Shift + Ctrl попробуйте')
        elif b == 'five':
            print('Совсем никак не меняется?(')
    else:
        print("Ошибка, попробуйте заново")
else:
    print("Ошибка, попробуйте заново")