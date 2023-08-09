"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=5&id_topic=113&id_problem=691
"""
b = int(input())
d = input().split()
c = input()
co = 0
for i in d:
    if i == c:
        co += 1
print(co)