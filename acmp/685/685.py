"""
https://acmp.ru/index.asp?main=task&id_task=685
"""
a1, a2, a3, b1, b2, b3 = map(int, input().split())
a = [a1, a2, a3]
b = [b1, b2, b3]
summa = 0
summa += max(a) * max(b)
a.remove(max(a))
b.remove(max(b))
summa += min(a) * min(b)
a.remove(min(a))
b.remove(min(b))
for el in a:
    for ele in b:
        summa += el * ele
print(summa)