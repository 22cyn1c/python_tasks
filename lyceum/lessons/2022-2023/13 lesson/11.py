n, s = input().split()
n = int(n)
s = int(s)
m = 0
kos = []
for i in range(n):
    p, k, c = input().split()
    p = int(p)
    k = int(k[1:])
    c = int(c[1:])
    m += p * k
    if p * k != c:
        kos.append(i + 1)
print(s - m)
print(*kos)