import random


n = int(input())
a = input().split()
b = input().split()
m = list(map(int, input().split(', ')))
c = 0
d = 0
e = 0
f = 0
for i in range(n):
    c = random.choice(a)
    while c in a:
        a.remove(c)
    d = random.choice(b)
    while d in b:
        b.remove(d)
    e = random.choice(range(m[0], m[1]))
    f = random.choice(range(1, 75))
    f = f / 10
    u = round(e * e * f, 1)
    print(f'Sandwich {c} and {d}, {e} cm, thickness {f} cm, usefulness {u}.')