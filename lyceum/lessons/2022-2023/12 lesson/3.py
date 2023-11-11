a = input()
b = input()
cb = 0
ck = 0
set_a = set()
set_b = set()
for i in range(len(a)):
    if a[i] == b[i]:
        cb += 1
    else:
        set_a.add(a[i])
        set_b.add(b[i])
c = set_a & set_b
print(cb, len(c))