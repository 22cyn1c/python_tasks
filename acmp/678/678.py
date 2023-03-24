"""
https://acmp.ru/index.asp?main=task&id_task=678
"""
c = 1
a = input()
for i in a:
    if c == 1:
        if i == 'A':
            c = 2
        elif i == 'C':
            c = 3
    elif c == 2:
        if i == 'A':
            c = 1
        elif i == 'B':
            c = 3
    elif c == 3:
        if i == 'B':
            c = 2
        elif i == 'C':
            c = 1
print(c)