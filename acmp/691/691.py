"""
https://acmp.ru/index.asp?main=task&id_task=691
"""
n = int(input())
b = 'ABCEHKMOPTXYАВСЕНКМОРТХ'
c = '1234567890'
for i in range(n):
    a = input()
    if len(a) == 6:
        if a[0] in b and a[4] in b and a[5] in b and a[1] in c and a[2] in c and a[3] in c:
            print('Yes')
        else:
            print('No')
    else:
        print('No')