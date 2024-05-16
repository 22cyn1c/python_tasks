"""
https://acmp.ru/index.asp?main=task&id_task=6
"""

a = input()
b = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
if (len(a) != 5 or a[2] != '-' or a[1] not in '12345678' or a[4] not in '12345678'
        or a[0] not in b or a[3] not in b):
    print('ERROR')
else:
    if max(b.index(a[0]), b.index(a[3])) - min(b.index(a[0]), b.index(a[3])) == 1:
        if max(int(a[1]), int(a[4])) - min(int(a[1]), int(a[4])) == 2:
            print('YES')
        else:
            print('NO')
    elif max(b.index(a[0]), b.index(a[3])) - min(b.index(a[0]), b.index(a[3])) == 2:
        if max(int(a[1]), int(a[4])) - min(int(a[1]), int(a[4])) == 1:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')