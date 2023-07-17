"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=3&id_section=23&id_topic=98&id_problem=499
"""
a = input().split('.')
a = a[:-1]
for i in range(len(a)):
    a[i] = a[i].split()
    b = a[i][::-1]
    print(*b, end='. ')