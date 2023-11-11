n = int(input())
s = []
for i in range(n):
    a = int(input())
    s.append(a)
b = 0
c = 0
t = -1
ss = []
for el in s:
    if t == -1:
        t = el
    else:
        b = el
        c = b + t
        t = el
        ss.append(c)
for elem in ss:
    print(elem)