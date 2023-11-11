a = input().split()
b = input().split()
d = []
f = 0
c = False
for i in range(len(a)):
    e = int(a[i]) - 1
    d.append(b[e])
print(' '.join(d).capitalize())