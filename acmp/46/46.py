"""
https://acmp.ru/index.asp?main=task&id_task=46
"""
e = '2.7182818284590452353602875'
n = int(input())
if n == 0:
    print(3)
elif n == 25:
    print(e)
elif int(e[n + 2]) < 5:
    print(e[:n + 2])
else:
    if int(e[n + 1]) == 9:
        print(e[:n + 2] + '0')
    else:
        print((e[:n + 1]) + str(int(e[n + 1]) + 1))