"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=27&id_problem=158
"""
a, b = map(int, input().split())
if b % a == 0:
    print(b // a, 0, 0)
else:
    print(b // a, b % a, a - b % a)