"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=41&id_problem=270
"""
a = input()
b = []
for i in a:
    b.append(i)
co = 0
for i in range(len(a)):
    if len(a) - 1 < i + 4:
        continue
    if a[i] == '>' and a[i + 1] == '>' and a[i + 2] == '-' and a[i + 3] == '-' and a[i + 4] == '>':
        co += 1
    elif a[i] == '<' and a[i + 1] == '-' and a[i + 2] == '-' and a[i + 3] == '<' and a[i + 4] == '<':
        co += 1
print(co)