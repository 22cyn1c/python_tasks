"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=41&id_problem=269
"""
a = input().split('.')
e = True
if len(a) != 4:
    e = False
    print('Bad')
for i in a:
    if i.isdigit():
        if not 0 <= int(i) <= 255:
            e = False
            print('Bad')
            break
    else:
        e = False
        print('Bad')
        break
if e:
    print('Good')