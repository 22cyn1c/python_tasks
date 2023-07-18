"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=3&id_section=23&id_topic=90&id_problem=461
"""
x, y = map(int, input().split())
if x > 0:
    if y > 0:
        print(1)
    elif y < 0:
        print(4)
    else:
        print('1 4')
elif x < 0:
    if y > 0:
        print(2)
    elif y < 0:
        print(3)
    else:
        print('2 3')
else:
    if y > 0:
        print('1 2')
    elif y < 0:
        print('3 4')
    else:
        print('1 2 3 4')