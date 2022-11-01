a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a + b > c and a + c > b and c + b > a:
    print('YES')
else:
    print('NO')
'''
https://acmp.ru/index.asp?main=task&id_task=606
'''