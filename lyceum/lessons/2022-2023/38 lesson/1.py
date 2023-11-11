import sys


a = []
for i in sys.stdin:
    a.append(i.split())
b = sorted(a, key=lambda x: (len(x), -a.index(x)))
b = b[::-1]
for i in range(len(a)):
    print(*b[i][:3])