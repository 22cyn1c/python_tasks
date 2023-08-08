"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=4&id_topic=38&id_problem=1197
"""
a = input()
b = []
for i in a:
    if i == 'z':
        b.append('a')
    else:
        b.append(chr(ord(i) + 1))
print(*b, sep='')