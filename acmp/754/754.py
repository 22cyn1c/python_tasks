"""
https://acmp.ru/index.asp?main=task&id_task=754
"""
b = True
s = list(map(int, input().split()))
for el in s:
    if not 93 < el < 728:
        print('Error')
        b = False
        break
if b:
    print(max(s))