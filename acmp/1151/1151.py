"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=41&id_problem=268
"""
a = 'qwertyuiopasdfghjklzxcvbnm'
b = 'QWERTYUIOPASDFGHJKLZXCVBNM'
c = '12345678890'
d = input()
e = False
f = False
j = False
if len(d) <= 11:
    print('No')
else:
    for i in range(0, len(d)):
        if d[i] in a:
            e = True
        if d[i] in b:
            f = True
        if d[i] in c:
            j = True
    if e and f and j:
        print('Yes')
    else:
        print('No')
