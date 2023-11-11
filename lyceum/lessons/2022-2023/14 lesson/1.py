n = int(input())
c = []
c1 = []
for i in range(n):
    a = input()
    c.append(a)
for el in c:
    print(el)
print()
for el in c:
    if '4' in el or '5' in el:
        print(el)