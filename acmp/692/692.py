a = int(input())
n = 2
b = 0
t = 0
if a == 0:
    print('NO')
elif a == 1:
    print('YES')
else:
    while a > t:
        b += 1
        t = n**b
    if a == t:
        print('YES')
    else:
        print("NO")
'''
https://acmp.ru/index.asp?main=task&id_task=692
'''