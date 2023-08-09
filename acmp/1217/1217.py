"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=113&id_problem=694
"""
a = int(input())
b = list(map(int, input().split()))
c = b[:]
for i in range(a):
    if b[i] == max(b):
        c[i] = min(b)
print(*c)