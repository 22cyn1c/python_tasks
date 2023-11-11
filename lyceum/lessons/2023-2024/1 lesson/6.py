import sys


a = input()
a1 = []
for i in a:
    a1.append(i.rstrip())
b = a1[:]
c = 0
d = True
e = []
j = 0
for i in sys.stdin:
    i = i.rstrip()
    for f in i:
        if f in b:
            b.remove(f)
            d = True
            j += 1
        else:
            d = False
            break
    if d:
        c += 1
        e.append(i)
    b = a1[:]
    d = True
print(c)
for i in e:
    print(i)