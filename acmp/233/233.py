n = int(input())
b = 0
if n == 1:
    a = int(input())
    if a <= 437:
        print('Crash', 1)
    else:
        print('No crash')
else:
    arr = list(map(int, input().split()))
    for i in range(n):
        if arr[i] <= 437:
            print('Crash', i + 1)
            b = 1
            break
    if b == 0:
        print('No crash')
"""
https://acmp.ru/index.asp?main=task&id_task=233
"""