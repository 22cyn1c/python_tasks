"""
https://acmp.ru/asp/do/index.asp?main=topic&id_course=3&id_section=22&id_topic=172
"""
a, b, c, d = map(int, input().split())
e = 0
f = 0
if a == 1:
    e += 2
else:
    f += 2
if b == 1:
    e += 1
else:
    f += 1
if d == 1:
    e += 1
else:
    f += 1
if c == 1:
    e += 1
else:
    f += 1
if e > f:
    print('Yes')
else:
    print('No')