"""
https://acmp.ru/index.asp?main=task&id_task=794
"""
a, b = map(int, input().split())
c = input()
if c == 'freeze':
    print(min(a, b))
elif c == 'heat':
    print(max(a, b))
elif c == 'auto':
    print(b)
else:
    print(a)