"""
https://acmp.ru/asp/do/index.asp?main=topic&id_course=3&id_section=22&id_topic=314
"""
a = int(input())
b = int(input())
c = int(input())
a1 = min(a, b, c)
b1 = (a + b + c) - min(a, b, c) - max(a, b, c)
c1 = max(a, b, c)
print(a1 + b1 - c1)