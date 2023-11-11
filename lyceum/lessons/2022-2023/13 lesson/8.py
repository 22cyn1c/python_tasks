n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
n = int(input()) - 1
m = int(input())
summa = 0
for el in s[n:m]:
    summa += el
print(summa)