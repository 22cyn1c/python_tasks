"""
https://acmp.ru/index.asp?main=task&id_task=550
"""
m = int(input())
if m % 400 == 0:
    print('12/09/' + '0' * (4 - len(str(m))) + str(m))
elif m % 4 == 0 and m % 100 != 0:
    print('12/09/' + '0' * (4 - len(str(m))) + str(m))
else:
    print('13/09/' + '0' * (4 - len(str(m))) + str(m))