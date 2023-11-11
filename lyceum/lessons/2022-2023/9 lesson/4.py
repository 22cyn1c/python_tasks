n = int(input())
n1 = int(input())
set_n = set()
set_n1 = set()
for i in range(n):
    a = input()
    if a in set_n:
        set_n1.add(a)
    else:
        set_n.add(a)
for i in range(n1):
    a = input()
    if a in set_n1:
        set_n.add(a)
    else:
        set_n1.add(a)
b = len(set_n ^ set_n1)
if b != 0:
    print(b)
else:
    print('NO')