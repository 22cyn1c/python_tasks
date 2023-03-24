"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=1&id_topic=27&id_problem=157
"""
a, b = map(int, input().split())
m = a * b
if a > 0:
    if m > 109:
        while m > 109:
            m -= 109
    print(m + 1)
else:
    if m * -1 > 109:
        while m * -1 > 109:
            m += 109
    print(109 + m + 1)