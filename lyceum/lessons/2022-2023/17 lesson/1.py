n = int(input())
e = []
for i in range(n):
    a = int(input())
    e.append(a)
a = int(input())
b = int(input())
for el in e:
    if a <= el <= b:
        print(el)