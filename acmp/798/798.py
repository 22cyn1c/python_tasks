"""
https://acmp.ru/index.asp?main=task&id_task=798
"""
m, n, i, j, c = map(int, input().split())
if (m * n) % 2 == 0:
    print('equal')
else:
    if (i + j) % 2 == 0:
        if c == 0:
            print('black')
        else:
            print('white')
    else:
        if c == 0:
            print('white')
        else:
            print('black')