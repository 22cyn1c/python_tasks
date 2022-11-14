n = int(input())
for i in range(n):
    a = input()
    if a[5] == '0':
        if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]) + 1 or int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + 9:
            print('Yes')
            continue
        else:
            print('No')
    elif a[5] == '9':
        if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) or int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]) - 1:
            print('Yes')
            continue
        else:
            print('No')
    else:
        if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]) + 1 or int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]) - 1:
            print('Yes')
            continue
        else:
            print('No')
"""
https://acmp.ru/index.asp?main=task&id_task=327
"""