n = int(input())
b = []
for i in range(n):
    a = input()
    b.append(a)
n = int(input())
for el in b:
    if len(el) >= n:
        print(el[n - 1], end='')