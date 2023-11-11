n = int(input())
n1 = int(input())
set_n = set()
set_n1 = set()
b = 0
for i in range(n):
    a = input()
    set_n.add(a)
for i in range(n1):
    a = input()
    set_n1.add(a)
    if set_n1 & set_n != set():
        print('YES')
    else:
        print('NO')
    set_n1 = set()
    b += 1