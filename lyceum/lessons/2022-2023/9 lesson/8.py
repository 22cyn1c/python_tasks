n = int(input())
set_a = set()
set_n = set()
b = 0
t = 0
c = set()
for i in range(n):
    a = input()
    if a in set_a:
        b += 1
        set_n.add(a)
    else:
        set_a.add(a)
c = len(set_a & set_n)
print(b + c)