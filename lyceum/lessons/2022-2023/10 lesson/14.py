a = input()
b = input()
if a[-1] == 'ь':
    if a[-2] == b[0]:
        print('ВЕРНО')
    else:
        print("НЕВЕРНО")
else:
    if a[-1] == b[0]:
        print('ВЕРНО')
    else:
        print("НЕВЕРНО")