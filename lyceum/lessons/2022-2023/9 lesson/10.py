a = int(input())
set_b = set()
set_n = set()
for i in range(a):
    b = input()
    set_b.add(b)
c = int(input())
for i in range(c):
    e = int(input())
    for j in range(e):
        n = input()
        set_n.add(n)
f = set_b - set_n
for elem in f:
    print(elem)