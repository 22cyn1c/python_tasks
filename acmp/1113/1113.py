"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=27&id_problem=156
"""
a, b = map(int, input().split())
if max(a, b) % min(a, b) == 0:
    print(1)
else:
    print(2)