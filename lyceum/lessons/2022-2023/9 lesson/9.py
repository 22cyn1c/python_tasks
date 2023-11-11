a = int(input())
set_b = set()
set_n = set()
for i in range(a):
    b = input()
    set_b.add(b)
c = int(input())
for i in range(c):
    d = input()
    e = int(input())
    for j in range(e):
        n = input()
        set_n.add(n)
    f = set_n & set_b
    if f == set_n:
        print(d)
    set_n = set()