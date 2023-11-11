n = int(input())
n1 = int(input())
n2 = int(input())
set_n = set()
set_n1 = set()
set_n2 = set()
for i in range(n):
    a = input()
    if a in set_n:
        if a in set_n1:
            set_n2.add(a)
        else:
            set_n1.add(a)
    else:
        set_n.add(a)
for i in range(n1):
    a = input()
    if a in set_n1:
        if a in set_n:
            set_n2.add(a)
        else:
            set_n.add(a)
    else:
        set_n1.add(a)
for i in range(n2):
    a = input()
    if a in set_n2:
        if a in set_n:
            set_n1.add(a)
        else:
            set_n.add(a)
    else:
        set_n2.add(a)
b = set_n & set_n1 & set_n2
c = set_n & set_n1
d = set_n & set_n2
e = set_n1 & set_n2
c = c - b
d = d - b
e = e - b
if len(c) + len(d) + len(e) != 0:
    print(len(c) + len(d) + len(e))
else:
    print('NO')