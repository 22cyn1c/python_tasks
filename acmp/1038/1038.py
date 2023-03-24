"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=27&id_problem=151
"""
a = int(input())
if a % 10 == 0:
    print(a // 10)
else:
    print(a // 10 + 1)